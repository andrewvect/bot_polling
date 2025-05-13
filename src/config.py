import dotenv
import os

dotenv.load_dotenv()
try:
    BOT_TOKEN = os.getenv("BOT_TOKEN")
except KeyError:
    raise KeyError("BOT_TOKEN environment variable is not set")

PORT = int(os.getenv("PORT", 3000))
WEBHOOK_URL = os.getenv("WEBHOOK_URL", 'webhook')
TESTING = os.getenv("TESTING", False)