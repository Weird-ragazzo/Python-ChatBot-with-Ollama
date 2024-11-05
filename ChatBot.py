import requests

def get_response(prompt):
    # Replace with your actual API endpoint
    url = "http://127.0.0.1:11434/api/generate"  
    data = {
        "model": "llama3.2:1b",
        "prompt": prompt,
        "stream": False
    }
    try:
        # Sending a POST request to the API
        response = requests.post(url, json=data)
        # Checking if the response is successful
        if response.status_code == 200:
            return response.json().get('response', 'No response found')
        else:
            print(f"Error: Received status code {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None

def chat():
    print("Chatbot: Hello! How can I assist you today? Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("ChatBot: Goodbye!")
            break

        response = get_response(user_input)
        if response:
            print(f"ChatBot: {response}")
        else:
            print("Chatbot: Sorry, I couldn't process that.")

if __name__ == "__main__":
    chat()