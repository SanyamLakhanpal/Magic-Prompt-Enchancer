import os
import requests
import json
from modules.utils.helper import build_input_prompt

zephyr_7b_beta = "https://api-inference.huggingface.co/models/HuggingFaceH4/zephyr-7b-beta/"

HF_TOKEN = os.getenv("HF_TOKEN")
HEADERS = {"Authorization": f"Bearer {HF_TOKEN}"}

def post_request_beta(payload):
    response = requests.post(zephyr_7b_beta, headers=HEADERS, json=payload)
    response.raise_for_status()
    return response.json()
