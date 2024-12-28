import os
from typing import Optional
from dotenv import load_dotenv, find_dotenv

_env_loaded = False

def load_env() -> bool:
    global _env_loaded
    if not _env_loaded:
        _env_loaded = load_dotenv(find_dotenv())
    return _env_loaded

def get_env(key: str, default: Optional[str] = None) -> Optional[str]:
    load_env()
    return os.getenv(key, default)


if __name__ == "__main__":
    print("Azure AI Interface")