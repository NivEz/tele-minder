import requests
from dotenv import load_dotenv
import os

load_dotenv()

# constants
BASE_URL = "https://api.telegram.org/bot"
TELEGRAM_TOKEN = os.environ["TELEGRAM_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]
METHOD = "sendMessage"
MESSAGE = "תקפיץ את המודעה!"
TELEGRAM_ERROR_MESSAGE = "A Telegram error has occurred..."


def build_telegram_request_url(base_url, token, telegram_method):
    return f"{base_url}{token}/{telegram_method}"


def send_telegram_message(chat_id, message):
    """Returns True if the message was sent successfully"""
    url = build_telegram_request_url(BASE_URL, TELEGRAM_TOKEN, METHOD)
    body = {
        'chat_id': chat_id,
        'text': message
    }
    res = requests.post(url, data=body)
    if res.status_code == 200:
        return True


def teleminder():
    is_sent = send_telegram_message(CHAT_ID, MESSAGE)
    if not is_sent:
        print(TELEGRAM_ERROR_MESSAGE)
        send_telegram_message(CHAT_ID, TELEGRAM_ERROR_MESSAGE)
        raise RuntimeError(TELEGRAM_ERROR_MESSAGE)


if __name__ == '__main__':
    teleminder()
