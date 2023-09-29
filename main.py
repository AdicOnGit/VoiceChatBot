from chat_api.response_handeler import ChatCompletion
from pywhispercpp.examples.assistant import Assistant
import json


def res_handler(e):
    print(e)
    chat.complete_prompt(e)

if __name__ == "__main__":
    with open("data_files/language.json", "r") as file:
        data = file.read()
        python_data = json.loads(data)
        print("---------Languages---------")
        for key, value in python_data.items():
            print(f"{key}:{value}")
        print("---------All languagues are not equally supported---------")
    prompt_type = "general_prompt"
    while True:
        language = input("Language(en for english): ")
        if language and language in python_data.keys():
            if language == "ja":
                prompt_type = "main_prompt"
            break
    chat = ChatCompletion(language, prompt_type)
    my_assistant = Assistant(commands_callback=res_handler, n_threads=8, language=language, model="small", silence_threshold=40)
    my_assistant.start()