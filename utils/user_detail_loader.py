import json
from typing import Literal


def user_detail_loader(detail_about:Literal["user_name", "last_logged_in", "user_level"]):
    try:
        with open("./user_detail.json", "r") as f:
            data = f.read()
            json_data = json.loads(data)
            return json_data.get(detail_about, "")
    except Exception as e:
        print(e)
        return None
