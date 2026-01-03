from scripts.SYS_Config.Config import DECISION_MODEL_PATH
from llama_cpp import Llama

# Module-level singleton
_router_llm = None

def logic_engine_init():
    """
    Initialize the router LLM once and reuse it.
    """
    global _router_llm

    if _router_llm is None:
        _router_llm = Llama(
            model_path=DECISION_MODEL_PATH,
            n_ctx=32768,
            n_threads=2,
            n_gpu_layers=-1,
            n_batch=3524,
            temperature=0.0,
            logits_all=False,
            verbose=False
        )

    return _router_llm


# Optional: auto-init on import (recommended)
router_llm = logic_engine_init()

# Usage 

# from scripts.Engine.Logic_Unit.Logic_Engine.main import router_llm
