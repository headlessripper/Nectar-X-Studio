import json
import scripts.SYS_PROMPTS.sys_msgs as sys_msgs


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