from chat_api.headers_payload_loader import headers_payload_loader
import requests
import brotli
from audio import text_to_audio
from typing import Literal

class ChatCompletion:
    def __init__(self, language, prompt_type:Literal["main_prompt", "first_greeting", "indonesia_prompt", "general_prompt"]) -> None:
        self.URL = "https://chat.aivvm.com/api/chat"
        self.messages = []
        self.language = language
        self.prompt_type = prompt_type
    
    def _headers_payload(self, message):
        if self.language == "ja":
            self.messages = [{"role": "system", "content": "Greet the user, introduce yourself and instead of merely listing out details, present them as if you're conversing with someone and clarifying concepts. These are common 20 words: 午前 近く 書く 自分 成る 教室 習う 公園 百 食べ物 明るい 塩 生徒 覚える 元気 更新 分別 縺れる 暑い 大丈夫 . Take time for each words and teach them throughly."}]
        self.messages.append({"role": "user", "content": message})
        return headers_payload_loader(self.messages, self.prompt_type)
    
    def _send_sentence_to_audio(self, sentence_to_send, punctuations, response_message):
        full_message = sentence_to_send + response_message
        for punc in punctuations:
            while punc in full_message:
                split_point = full_message.index(punc) + len(punc)
                final_sentence = full_message[:split_point].strip("*")
                text_to_audio(final_sentence, language=self.language)
                full_message = full_message[split_point:]
                if not full_message:  # If there's no text left after splitting
                    break
        return full_message

    
    def _process_response_content(self, response):
        assistant_message = []
        sentence_to_send = ""
        punctuations = ["。", "！", "？", "…", "・", '.', '!','?', "।","۔"]
        for chunk in response.iter_content(chunk_size=None):
            if chunk:
                try:
                    decompressed_chunk = brotli.decompress(chunk)
                    response_message = decompressed_chunk.decode('utf-8')
                except Exception as e:
                    response_message = chunk.decode('utf-8')
                sentence_to_send = self._send_sentence_to_audio(sentence_to_send, punctuations, response_message)
                assistant_message.append(response_message)
        return "".join(assistant_message).replace("\n", "").replace("*", "")
    
    def complete_prompt(self, prompt):
        headers, payload = self._headers_payload(prompt)
        with requests.post(url=self.URL, headers=headers, json=payload, stream=True) as response:
            response.raise_for_status()
            response_message = self._process_response_content(response)
            self.messages.append({"role": "assistant", "content": response_message})
            return response_message