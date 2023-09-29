from fake_useragent import UserAgent
from chat_api.get_cookies import get_cookies
from utils.prompt_loader import prompt_loader


cookie = get_cookies()

def headers_payload_loader(messages, prompt_type):
    if not cookie:
        return None
    ua = UserAgent()

    headers = {
    "authority": "chat.aivvm.com",
    "method": "POST",
    "path": "/api/chat",
    "scheme": "https",
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
    "Content-Type": "application/json",
    "Cookie": f"cf_clearance={cookie}",
    "Origin": "https://chat.aivvm.com",
    "Referer": "https://chat.aivvm.com/",
    "User-Agent": ua.random
    }

    payload = {
        "model": {
            "id": "gpt-4-32k-0613",
            "name": "GPT-4-32K-0613"
        },
        "messages": messages,
        "key": "",
        "prompt": prompt_loader(prompt_type),
        "temperature": 1
    }

    return headers, payload