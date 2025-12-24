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
print(TELEGRAM_BOT_TOKEN)