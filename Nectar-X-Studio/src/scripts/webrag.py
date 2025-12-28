import asyncio
import requests
from datetime import datetime
from winotify import Notification, audio
import feedparser
import torch
import re
from datetime import datetime
from sentence_transformers import SentenceTransformer, util
from concurrent.futures import ThreadPoolExecutor, as_completed
from bs4 import BeautifulSoup

from scripts.components.Utility.write_to_log import write_to_log
from scripts.components.Service.find_icon import find_icon
from scripts.SYS_Config.Config import TRANSFORMER_MODEL_PATH


# ----------- Web RAG -----------

# FIXED: Safe GPU initialization with error handling + memory management
def load_embedding_model_safely(model_path):
    try:
        # Check CUDA availability and version
        if torch.cuda.is_available():
            write_to_log(f"CUDA available Posting: {torch.cuda.get_device_name(0)}")
            write_to_log(f"CUDA version Booting: {torch.version.cuda}")
        
            torch.cuda.empty_cache()  # Clear any existing cache
            torch.cuda.synchronize()  # Sync CUDA operations
        
        device = 'cuda' if torch.cuda.is_available() else 'cpu'
        write_to_log(f"Loading engine model on device: {device}")
        toast = Notification(
            app_id="Nectar-X-Studio",
            title="WebRAG Engine",
            msg=f"Loading engine model on device: {device}",
            icon=find_icon('background/NectarX.png'),
            duration="short"
        )
        toast.set_audio(audio.SMS, loop=False)
        toast.show()
        
        model = SentenceTransformer(model_path, device=device)
        
        # Warmup to catch CUDA issues early
        dummy_text = ["test"]
        model.encode(dummy_text, batch_size=1, show_progress_bar=False)
        write_to_log("Engine Model loaded and warmed up successfully!")
        toast = Notification(
            app_id="Nectar-X-Studio",
            title="WebRAG Engine",
            msg=f"Engine Model loaded and warmed up successfully!",
            icon=find_icon('background/NectarX.png'),
            duration="short"
        )
        toast.set_audio(audio.SMS, loop=False)
        toast.show()
        return model, device
        
    except Exception as e:
        write_to_log(f"GPU failed ({e}), falling back to CPU")
        toast = Notification(
            app_id="Nectar-X-Studio",
            title="WebRAG Engine",
            msg=f"GPU failed ({e}), falling back to CPU",
            icon=find_icon('background/NectarX.png'),
            duration="short"
        )
        toast.set_audio(audio.SMS, loop=False)
        toast.show()
        torch.cuda.empty_cache() if torch.cuda.is_available() else None
        return SentenceTransformer(model_path, device='cpu'), 'cpu'

embedding_model, device = load_embedding_model_safely(TRANSFORMER_MODEL_PATH)

class WebRAG:
    def __init__(self, rag_engine, google_api_key="AIzaSyD4Au69N-YV36kXA3g1YQcD-n55jpFf6Y8", google_cse_id="117a05283b97b4f08"):
        self.rag_engine = rag_engine
        self.google_api_key = google_api_key
        self.google_cse_id = google_cse_id
        self.session = requests.Session()
        self.session.headers.update({"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"})

    def __del__(self):
        if hasattr(self, 'session'):
            self.session.close()
        torch.cuda.empty_cache()  # Clean GPU memory

    # ------------------ Google News search ------------------
    def google_news_search(self, query, when="1d", max_results=5):
        q = requests.utils.quote(query)
        url = f"https://news.google.com/rss/search?q={q}&hl=en-US&gl=US&ceid=US:en"
        feed = feedparser.parse(url)
        entries = feed.entries[:max_results]
        news_results = []
        for e in entries:
            news_results.append({
                "link": getattr(e, "link", ""),
                "title": getattr(e, "title", ""),
                "snippet": getattr(e, "summary", ""),
                "published": getattr(e, "published", "")
            })
        return news_results

    # ------------------ Google Search with Default Recency ------------------
    def google_search(self, query, max_results=5, recent="m1"):
        if not self.google_api_key or not self.google_cse_id:
            raise ValueError("Google API key and CSE ID are required for Google search.")
        search_results = []
        url = "https://www.googleapis.com/customsearch/v1"
        params = {
            "key": self.google_api_key,
            "cx": self.google_cse_id,
            "q": query,
            "num": min(max_results, 10)
        }
        params["dateRestrict"] = recent
        response = self.session.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        for item in data.get("items", []):
            search_results.append({
                "link": item.get("link"),
                "snippet": item.get("snippet", ""),
                "displayLink": item.get("displayLink", "")
            })
        return search_results

    # ------------------ Concurrent Page Fetching ------------------
    def fetch_pages_concurrent(self, urls, max_workers=8, max_chars=4000):  # Reduced workers
        def fetch_single(url):
            try:
                resp = self.session.get(url, timeout=8)  # Reduced timeout
                resp.raise_for_status()
                soup = BeautifulSoup(resp.text, "html.parser")
                for tag in soup(["script", "style", "nav", "footer", "header"]):
                    tag.decompose()
                return " ".join(soup.stripped_strings)[:max_chars]
            except Exception:
                return ""
        
        if not urls:
            return []
        
        pages = [None] * len(urls)
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            future_to_idx = {executor.submit(fetch_single, url): i for i, url in enumerate(urls)}
            for future in as_completed(future_to_idx):
                idx = future_to_idx[future]
                pages[idx] = future.result()
        return pages

    # ------------------ FIXED Validation with Safe GPU Encoding ------------------
    def validate_results(self, query, results):
        if not results:
            return []

        now = datetime.now()
        current_year = str(now.year)
        outdated_keywords = ["Snapdragon 8 Gen 2", "Snapdragon 8 Gen 3", "2023", "2022"]
        tech_domains = ["samsung.com", "gsmarena.com", "techradar.com", "91mobiles.com", "phonearena.com", "sammyfans.com"]

        # 1) Concurrently fetch pages
        urls = [r["link"] for r in results]
        page_texts = self.fetch_pages_concurrent(urls)

        # 2) Build texts + filter outdated
        texts = []
        valid_indices = []
        for i, r in enumerate(results):
            page_text = page_texts[i] or ""
            text = r["snippet"] + " " + page_text
            
            if any(keyword.lower() in text.lower() for keyword in outdated_keywords):
                continue
            
            texts.append(text)
            valid_indices.append(i)

        if not texts:
            return []

        # 3) SAFE GPU encode with error handling + smaller batch
        try:
            if device == 'cuda':
                torch.cuda.empty_cache()
            
            # Smaller batch_size for stability + normalize_embeddings=False
            text_embs = embedding_model.encode(
                texts, 
                batch_size=16,  # Reduced from 32
                show_progress_bar=False, 
                convert_to_tensor=True,
                normalize_embeddings=True
            )
            
            if device == 'cuda':
                torch.cuda.empty_cache()
                
        except RuntimeError as e:
            if "CUDA" in str(e):
                print(f"GPU encoding failed: {e}. Falling back to CPU.")
                torch.cuda.empty_cache()
                text_embs = embedding_model.encode(
                    texts, 
                    batch_size=8, 
                    device='cpu',
                    show_progress_bar=False, 
                    convert_to_tensor=False
                )
            else:
                raise

        # 4) Score with bonuses
        query_emb = embedding_model.encode(query, batch_size=1, show_progress_bar=False, convert_to_tensor=True)
        scored_results = []

        for j, text in enumerate(texts):
            i = valid_indices[j]
            score = util.cos_sim(query_emb, text_embs[j]).item()
            
            # Recency parsing
            date_matches = re.findall(r'\b(2025|2024|2023|Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\b', text, re.I)
            recency_bonus = 0
            if current_year in date_matches:
                recency_bonus += 3.0
            elif "2024" in date_matches:
                recency_bonus += 1.5
            elif any(month in date_matches for month in ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']):
                recency_bonus += 1.0

            domain_bonus = 0.8 if any(domain in results[i].get("displayLink", "").lower() for domain in tech_domains) else 0

            total_score = score + recency_bonus + domain_bonus
            scored_results.append({
                "link": results[i]["link"],
                "snippet": results[i]["snippet"],
                "content": page_texts[i] or "",
                "score": total_score,
                "recency_bonus": recency_bonus,
                "domain_bonus": domain_bonus
            })

        scored_results.sort(key=lambda x: x["score"], reverse=True)
        return scored_results[:3]

    # ------------------ Add Web Docs to RAG ------------------
    def add_web_docs(self, query, num_results=5, recent="w1"):
        if not self.rag_engine:
            print("RAG engine not initialized")
            return

        try:
            search_results = self.google_search(query, num_results, recent)
        except Exception as e:
            print(f"Google web search failed: {e}")
            search_results = []

        try:
            news_results_raw = self.google_news_search(query, when="1d", max_results=num_results)
        except Exception as e:
            print(f"Google News search failed: {e}")
            news_results_raw = []

        news_results = [
            {
                "link": r["link"],
                "snippet": r.get("snippet", r.get("title", "")),
                "displayLink": r.get("link", "")
            }
            for r in news_results_raw
            if r.get("link")
        ]

        validated_web = self.validate_results(query, search_results)
        validated_news = self.validate_results(query, news_results)

        combined_validated = validated_web + validated_news
        if not combined_validated:
            # toast notification here
            return

        docs = []
        for result in combined_validated:
            combined_text = result["snippet"] + "\n\n" + result["content"]
            if combined_text.strip():
                docs.append(combined_text)

        if docs:
            self.rag_engine.add_documents(docs)
            top_score = combined_validated[0]["score"]
            toast = Notification(
                app_id="Nectar-X-Studio",
                title="WebRAG Info",
                msg=f"Added {len(docs)} recent web/news documents (top score: {top_score:.1f})",
                icon=find_icon('background/NectarX.png'),
                duration="short"
            )
            toast.set_audio(audio.SMS, loop=False)
            toast.show()
        else:
            toast = Notification(
                app_id="Nectar-X-Studio",
                title="WebRAG Warning",
                msg="No recent/relevant documents found. Try different query.",
                icon=find_icon('background/NectarX.png'),
                duration="short"
            )
            toast.set_audio(audio.SMS, loop=False)
            toast.show()