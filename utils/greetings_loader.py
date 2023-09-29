from utils.prompt_loader import prompt_loader
from utils.user_detail_loader import user_detail_loader


def greetings_loader(user_last_logged_in):
    if user_last_logged_in == "never":
        greeting_prompt = prompt_loader("first_greeting")
        return [{"role":"system", "content": greeting_prompt}]