import json
import scripts.SYS_PROMPTS.sys_msgs as sys_msgs
from scripts.SYS_Config.Config import DECISION_MODEL_PATH
try:
    from llama_cpp import Llama
except Exception:
    Llama = None

router_llm = Llama(
    model_path=DECISION_MODEL_PATH,
    n_ctx=32768,
    n_threads=2,
    n_gpu_layers=-1,
    n_batch=3524,
    temperature=0.0,
    logits_all=False,
    verbose=False
)

# ---------------------------------------------------------------
# 🔎 QUERY GENERATOR
# ---------------------------------------------------------------
def query_generator(query):
    """Generate a search query based on the last user prompt."""
    sys_msg = sys_msgs.query_msg
    query_msg = f"CREATE A SEARCH QUERY FOR THIS PROMPT:\n{query}"

    response = router_llm.create_chat_completion(
        messages=[
            {"role": "system", "content": sys_msg},
            {"role": "user", "content": query_msg},
        ],
        max_tokens=50,
        stop=["\n"],
    )

    return response["choices"][0]["message"]["content"].strip()

def model_decides_web_rag(llm, query: str) -> bool:

    messages = [
        sys_msgs.ROUTER_SYSTEM_PROMPT,
        {"role": "user", "content": query}
    ]

    result = llm.create_chat_completion(
        messages,
        max_tokens=50,
        temperature=0.0  # deterministic
    )

    raw = result["choices"][0]["message"]["content"].strip()

    try:
        decision = json.loads(raw)
        return bool(decision.get("use_web", False))
    except Exception:
        # Safety fallback: don't web-search
        return False