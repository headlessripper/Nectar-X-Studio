<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Nectar – Powered by Zashirion AI Engine</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      line-height: 1.6;
      margin: 20px;
      background-color: #f9f9f9;
      color: #222;
    }
    h1, h2, h3 {
      color: #333;
    }
    code, pre {
      background: #f4f4f4;
      padding: 10px;
      border-radius: 6px;
      display: block;
      overflow-x: auto;
    }
    ul {
      list-style: none;
      padding-left: 0;
    }
    ul li {
      margin: 8px 0;
    }
    .emoji {
      font-size: 1.2em;
      margin-right: 6px;
    }
    a {
      color: #0073e6;
      text-decoration: none;
    }
    a:hover {
      text-decoration: underline;
    }
    .section {
      margin-bottom: 30px;
    }
  </style>
</head>
<body>

  <h1>🌸 Nectar – Powered by Zashirion AI Engine</h1>

  <img src="https://github.com/user-attachments/assets/dc85d6ad-018f-4899-ac13-631c5ee8901f" 
       alt="NectarX" style="max-width: 100%; border-radius: 10px;">

  <p><strong>Nectar</strong> is a powerful, AI-enhanced application that seamlessly integrates with 
  <strong>LM Studio</strong> to bring <strong>local large language models</strong> to life—right on your own machine.</p>

  <p>With <strong>no internet connection required</strong>, Nectar ensures 
  <strong>privacy-first, high-performance inference</strong> using cutting-edge open-source models from 
  <strong>Hugging Face, Ollama, and beyond</strong>.</p>

  <p>Whether you’re generating natural language, analyzing text, or embedding AI into your workflows, 
  Nectar gives you <strong>full control</strong> over how and where your models run—optimized for 
  <strong>efficiency</strong> and <strong>user freedom</strong>.</p>

  <div class="section">
    <h2>🚀 Core Features</h2>
    <ul>
      <li>🔒 <strong>Offline Inference</strong> – Run LLMs locally with zero cloud dependency.</li>
      <li>⚡ <strong>Fast & Lightweight</strong> – Real-time performance on consumer hardware.</li>
      <li>🧩 <strong>Model Flexibility</strong> – Supports GGUF, GPTQ, and other formats with Hugging Face & Ollama integration.</li>
      <li>🖥️ <strong>Developer Ready</strong> – Use Nectar as your intelligent backend for automation, coding, content creation, or research.</li>
      <li>🛠️ <strong>Built on Zashirion AI Engine</strong> – With an intuitive UI and powerful API layer for embedding into custom workflows.</li>
    </ul>
    <p>✅ <strong>Ideal for</strong>: developers, researchers, cybersecurity experts, and power users who want 
    AI without sacrificing privacy or control.</p>
  </div>

  <div class="section">
    <h2>🔗 Nectar Interact API</h2>
    <p>📄 <a href="https://github.com/user-attachments/files/20288337/Nectar-API.txt" target="_blank">Nectar-API.txt</a></p>

    <h3>Example: Local Developer API Usage</h3>
    <pre><code>def send_to_AlphaLLM(question):
    import socket
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(("127.0.0.1", 5005))
        client.send(question.encode("utf-8"))
        response = client.recv(4096)
        client.close()
        return response.decode("utf-8")
    except (socket.error, socket.timeout) as e:
        return f"[Error] Could not connect to AlphaLLM: {e}"
</code></pre>
  </div>

  <div class="section">
    <h2>✨ Nectar-X-Studio</h2>
    <p><strong>Nectar-X-Studio</strong> is the extended, feature-rich edition of Nectar—your 
    <strong>self-hosted LLM inference suite</strong> for building agents, connecting knowledge, 
    and performing deep research.</p>

    <h3>🔥 Advanced Features</h3>
    <ul>
      <li>🤖 <strong>Custom Agents</strong> – Build AI agents with unique instructions, knowledge, and actions.</li>
      <li>🌍 <strong>Web Search</strong> – Integrates Google PSE, Exa, Serper, Firecrawl, and in-house scrapers.</li>
      <li>🔍 <strong>RAG</strong> – Hybrid search + knowledge graph for uploaded files & connected data sources.</li>
      <li>🔄 <strong>Connectors</strong> – Access 40+ apps for knowledge, metadata, and information retrieval.</li>
      <li>🔬 <strong>Deep Research</strong> – Multi-step, agentic search for in-depth answers.</li>
      <li>▶️ <strong>Actions & MCP</strong> – Allow AI agents to interact with external systems.</li>
      <li>💻 <strong>Code Interpreter</strong> – Execute Python for data analysis, graphing, and file generation.</li>
      <li>🎨 <strong>Image Generation</strong> – Create images from user prompts.</li>
      <li>👥 <strong>Collaboration Tools</strong> – Chat sharing, feedback, user management, usage analytics, and more.</li>
    </ul>

    <p><strong>Nectar-X-Studio</strong> works with <strong>all LLMs</strong> (OpenAI, Anthropic, Gemini, etc.) 
    and <strong>self-hosted models</strong> (Ollama, vLLM, etc.).</p>
  </div>

  <div class="section">
    <h2>📜 Changelog</h2>
    <p>🔗 <a href="https://github.com/headlessripper/Nectar/commits/v1.1" target="_blank">Full Changelog</a></p>
  </div>

</body>
</html>
