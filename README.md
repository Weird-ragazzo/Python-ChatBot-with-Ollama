# ChatBot 🤖💬

Welcome to the **ChatBot** project, a Python-based chatbot designed to engage users in natural language conversations! This project leverages the powerful Llama3.2:1b model from Ollama to provide intelligent responses and a seamless user experience.

## Features 🌟

- **Interactive Conversations**: Engage in dynamic conversations with the chatbot.
- **Powered by Llama3.2:1b**: Utilizes advanced AI model for natural language processing.
- **Easy to Use**: Simple setup and intuitive interaction through the command line.

## Technologies Used 🛠️

- **Python**: The main programming language used to build the chatbot.
- **Ollama**: Framework for running AI models.
- **Libraries**: Includes essential libraries like `requests` for handling HTTP requests.

## Small Intro about my Project:
This Python script creates an interactive chatbot that communicates with an AI model through a local API. Here’s a quick breakdown of how it works:

- **API Configuration**: The code sets up a connection to a local API endpoint (http://127.0.0.1:11434/api/generate), which serves as the brain of the chatbot.
- **Sending Requests**: Using the requests library, it sends a POST request with the user's prompt, specifying the model to use (llama3.2:1b).
- **Handling Responses**: If the API call is successful (HTTP 200), the chatbot retrieves and displays the generated response. If not, it provides an error message.
- **User Interaction**: The chat function initiates a conversation, greeting the user and prompting for input until they type "exit."
- **Graceful Exits**: Users can end the conversation smoothly, ensuring a friendly experience.

This code exemplifies how to build a simple yet powerful chatbot interface, allowing for easy expansion and customization!

## Getting Started 🚀

To run the ChatBot locally, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Weird-ragazzo/ChatBot.git

2. **Install llama3.2:1b model**:
   Install the Llama3.2:1b model from Ollama by running the following command in your command line:
  ```bash
  ollama run llama3.2:1b
```
3. **Run the Chatbot**:
  After starting the model in the background by using command:
  ```bash
  ollama run llama3.2:1b
  ```
 navigate to the project directory and run the Python script:
  ```bash
  cd ChatBot
  python ChatBot.py
  ```

4. **Start Chatting**:
  Begin interacting with your chatbot right away!

## Contributing 🤝
Contributions are welcome! If you have ideas for features or improvements, feel free to fork the repository and submit a pull request. 

## Contact 📫
For inquiries or feedback, you can reach me at dhruvraghav2003@gmail.com .

