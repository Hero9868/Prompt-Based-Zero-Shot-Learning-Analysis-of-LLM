
import requests
import json
import os

API_KEY = os.environ['API_KEY']

def inference(CUSTOM_PROMPT: str):
    req = requests.post(
        "https://api.ai21.com/studio/v1/j1-jumbo/complete",
        headers={"Authorization": f"Bearer {API_KEY}"},
        json={
            "prompt": f"{CUSTOM_PROMPT}", 
            "numResults": 1, 
            "maxTokens": 100,
            "topKReturn": 0,
            "topP":1,
            "stopSequences":['Input'],
            "temperature": 0.78
        }
    )
    return req.json()["completions"][0]['data']['text']