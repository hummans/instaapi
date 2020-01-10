import requests
import json
import re
import time
from .config import payload, headers

class Api:
    def __init__(self):
        pass

    def user_page(self, username):
        try:
            home = str(requests.post("https://instagram.com/" + username, data=json.dumps(payload), headers=headers).content)
        except Exception as e:
            print(e)
        return home
        
