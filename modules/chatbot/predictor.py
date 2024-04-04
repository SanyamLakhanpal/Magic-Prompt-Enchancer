from modules.utils.helper import build_input_prompt
from modules.post_request.requester import post_request_beta

def predict_beta(message, chatbot=[], system_prompt=""):
    input_prompt = build_input_prompt(message, chatbot, system_prompt)
    data = {
        "inputs": input_prompt
    }

    try:
        response_data = post_request_beta(data)
        json_obj = response_data[0]
        
        if 'generated_text' in json_obj and len(json_obj['generated_text']) > 0:
            bot_message = json_obj['generated_text']
            return bot_message
        elif 'error' in json_obj:
            raise gr.Error(json_obj['error'] + ' Please refresh and try again with smaller input prompt')
        else:
            warning_msg = f"Unexpected response: {json_obj}"
            raise gr.Error(warning_msg)
    except requests.HTTPError as e:
        error_msg = f"Request failed with status code {e.response.status_code}"
        raise gr.Error(error_msg)
    except json.JSONDecodeError as e:
        error_msg = f"Failed to decode response as JSON: {str(e)}"
        raise gr.Error(error_msg)
