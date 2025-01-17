# Script which checks telegram updates and sends it locally to the port number
import logging
import requests
import time
from typing import Dict, List

from config import BOT_TOKEN, PORT, WEBHOOK_URL


def get_updates(offset: int = None) -> list[dict]:
    """Get updates from Telegram server"""
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/getUpdates"
    params = {"timeout": 30}  # Long polling timeout
    if offset:
        params["offset"] = offset

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()["result"]
    except requests.RequestException as e:
        logging.error(f"Error getting updates: {e}")
        return []

def send_updates(updates: List[Dict[str, str]]) -> None:
    """Send updates to local server"""
    for update in updates:
        try:
            response = requests.post(f"http://host.docker.internal:{PORT}/{WEBHOOK_URL}", json=update)
            response.raise_for_status()
        except requests.RequestException as e:
            logging.error(f"Error sending update: {e}")
            pass

def main() -> None:
    logging.basicConfig(level=logging.INFO)
    logging.info("Starting the bot...")
    logging.info(f"Forwarding updates to local server {PORT}")

    offset = None
    while True:
        try:
            updates = get_updates(offset)
            if updates:
                offset = updates[-1]["update_id"] + 1  # Update offset to the highest update ID + 1
            send_updates(updates)
        except Exception as e:
            logging.error(f"Error in main loop: {e}")
            time.sleep(5)  # Wait before retrying on error


if __name__ == "__main__":
    main()
