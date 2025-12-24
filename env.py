import dotenv
import os
dotenv.load_dotenv()

def get_env_variable(key: str) -> str:
    value = os.getenv(key)
    if value is None:
        raise EnvironmentError(f"Environment variable '{key}' not found.")
    return value

TELEGRAM_BOT_TOKEN = get_env_variable("TELEGRAM_BOT_TOKEN")
OPENAI_API_KEY = get_env_variable("OPENAI_API_KEY")
GEMINI_API_KEY = get_env_variable("GEMINI_API_KEY")
FIRECRAWL_API_KEY = get_env_variable("FIRECRAWL_API_KEY")

NAVER_API_CLIENT_ID = get_env_variable("NAVER_API_CLIENT_ID")
NAVER_API_SECRET_KEY = get_env_variable("NAVER_API_SECRET_KEY")
GOOGLE_SEARCH_CX = get_env_variable("GOOGLE_SEARCH_CX")
GOOGLE_SEARCH_API_KEY = get_env_variable("GOOGLE_SEARCH_API_KEY")