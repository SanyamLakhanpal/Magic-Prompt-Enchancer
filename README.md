# 🌟 Magic Image Prompt Enhancer 🖼️

<img src="assets/mpe.png" alt="Alt text" title="Optional title" width="500" height="500">

The Magic Image Prompt Enhancer project enhances the user's short prompt with more details for the image generation process. It leverages the Zephyr-7b-beta model to generate detailed prompts based on user input.

## 💡 How it Works

1. **Input Prompt Enhancement:** The user provides a short prompt describing the desired image. This prompt serves as the input for the enhancement process.

2. **System Prompt Integration:** By default, the project uses the following system prompt to guide the prompt generation process:
    ```plaintext
    "As an LLM, your job is to generate detailed prompts that start with generate the image, for image generation models based on user input. Be descriptive and specific, but also make sure your prompts are clear and concise."
    ```

3. **Prompt Generation:** The user's short prompt and the system prompt are combined to form a comprehensive input prompt. This input prompt is then fed into the Zephyr-7b-beta model for prompt enhancement.

4. **Prompt Enhancement:** The Zephyr-7b-beta model processes the input prompt and generates a more detailed and descriptive prompt tailored for image generation models. This enhanced prompt provides additional context and guidance for the image generation process.

5. **Image Generation:** The enhanced prompt is used as input for image generation models, such as generative adversarial networks (GANs) or language-conditioned models. These models generate images based on the provided prompt, resulting in high-quality and contextually relevant image outputs.

## 🛠️ Installation

To use the Magic Image Prompt Enhancer, follow these steps:

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/SanyamLakhanpal/Magic-Prompt-Enchancer.git
    ```

2. Navigate to the project directory:

    ```bash
    cd magic-image-prompt-enhancer
    ```

3. Install the required dependencies using pip:

    ```bash
    pip install -r requirements.txt
    ```

## 🚀 Usage

Once the installation is complete, you can run the project by executing the main Python file:

```bash
python main.py
```

This will launch the user interface where you can input your short prompt and see the enhanced image generation process in action.

🤝 Contributing
Contributions to the Magic Image Prompt Enhancer project are welcome! If you'd like to contribute, please fork the repository, make your changes, and submit a pull request.

📝 License
This project is licensed under the MIT License. See the LICENSE file for details.


