import dotenv
import os

dotenv.load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
PORT = int(os.getenv("PORT", 3000))
WEBHOOK_URL = os.getenv("WEBHOOK_URL", 'webhook')