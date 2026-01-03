import scripts.SYS_PROMPTS.sys_msgs as sys_msgs

# ---------------------------------------------------------------
# 🔎 QUERY GENERATOR
# ---------------------------------------------------------------
def query_generator(llm, query):
    """Generate a search query based on the last user prompt."""
    sys_msg = sys_msgs.query_msg
    query_msg = f"CREATE A SEARCH QUERY FOR THIS PROMPT:\n{query}"

    response = llm.create_chat_completion(
        messages=[
            {"role": "system", "content": sys_msg},
            {"role": "user", "content": query_msg},
        ],
        max_tokens=50,
        stop=["\n"],
    )

    return response["choices"][0]["message"]["content"].strip()