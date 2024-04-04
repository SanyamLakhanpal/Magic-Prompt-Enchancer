def build_input_prompt(message, chatbot, system_prompt):
    input_prompt = "\n" + system_prompt + "</s>\n\n"
    for interaction in chatbot:
        input_prompt = input_prompt + str(interaction[0]) + "</s>\n\n" + str(interaction[1]) + "\n</s>\n\n"

    input_prompt = input_prompt + str(message) + "</s>\n"
    return input_prompt
