import gradio as gr
from modules.chatbot.predictor import predict_beta
import os

SYSTEM_PROMPT = os.getenv("SYSTEM_PROMPT")
TITLE = os.getenv("TITLE")
EXAMPLE_INPUT = os.getenv("EXAMPLE_INPUT")

welcome_preview_message = f"""
Expand your imagination and broaden your horizons with LLM. Welcome to **{TITLE}**!:\nThis is a chatbot that can generate detailed prompts for image generation models based on simple and short user input.\nSay something like: 

"{EXAMPLE_INPUT}"
"""

chatbot_preview = gr.Chatbot(layout="panel", value=[(None, welcome_preview_message)])
textbox_preview = gr.Textbox(scale=7, container=False, value=EXAMPLE_INPUT)

def test_preview_chatbot(message, history):
    response = predict_beta(message, history, SYSTEM_PROMPT)
    text_start = response.rfind("", ) + len("")
    response = response[text_start:]
    return response

demo = gr.ChatInterface(test_preview_chatbot, chatbot=chatbot_preview, textbox=textbox_preview)
demo.launch(share=True)
