import json
from typing import Literal

def prompt_loader(prompt_name:Literal["main_prompt", "first_greeting", "indonesia_prompt", "general_prompt"]):
    try:
        with open("./data_files/prompts.json", "r") as f:
            prompts = json.load(f)
            return prompts.get(prompt_name, "")
    except Exception as error:
        print(error)
        return None

