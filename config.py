VICUNA_PATH = ".../project/vicuna-13b-v1.5/" # ADD PATH
LLAMA_PATH = ".../project/Llama-2-7b-chat-hf" # ADD PATH

VICUNA_API_LINK ="https://..." # ADD LINK
LLAMA_API_LINK = "https://..." # ADD LINK


ATTACK_TEMP = 1
TARGET_TEMP = 0
ATTACK_TOP_P = 0.9
TARGET_TOP_P = 1
MAX_PARALLEL_STREAMS = 1

#INSERT DESIRED PATHS AND KEYS HERE
import os

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if OPENAI_API_KEY is None:
    raise ValueError("OPENAI_API_KEY is not set")
ANTHROPIC_API_KEY = ""