import openai
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Set OpenAI API key from environment variable
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("Error: OPENAI_API_KEY not found in .env file")
openai.api_key = api_key

def get_chatbot_response(user_input):
    """
    Fetches a response from OpenAI's gpt-3.5-turbo model for the given user input.
    Returns the model's response or an error message if something goes wrong.
    """
    if not user_input.strip():
        return "Please say something!"
    try:
        response = openai.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a friendly and helpful assistant."},
                {"role": "user", "content": user_input}
            ],
            max_tokens=150,  # Limits response length
            temperature=0.7  # Balances creativity and coherence
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    """
    Runs the AskLumina chatbot, allowing users to interact via the console.
    Type 'quit' to exit.
    """
    print("Welcome to AskLumina! Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            print("Goodbye from AskLumina!")
            break
        response = get_chatbot_response(user_input)
        print(f"Lumina: {response}")

if __name__ == "__main__":
    main()