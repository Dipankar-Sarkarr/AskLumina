from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Initialize OpenAI client with API key from environment variable
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("Error: OPENAI_API_KEY not found in .env file")

client = OpenAI(api_key=api_key)

def get_chatbot_response(user_input, previous_response_id=None):
    if not user_input.strip():
        return "Please say something!"
    try:
        response = client.responses.create(
            model="gpt-4o",
            instructions="You are a friendly and helpful assistant.",
            input=user_input,
            max_output_tokens=150,
            store=True,  # স্টেট সেভ করতে বলছে
            previous_response_id=previous_response_id  # আগের কথোপকথনের আইডি
        )
        return response.output_text.strip(), response.id  # রেসপন্স আর আইডি রিটার্ন করছে
    except Exception as e:
        return f"Error: {str(e)}", None

def main():
    print("Welcome to AskLumina! Type 'quit' to exit.")
    previous_response_id = None
    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            print("Goodbye from AskLumina!")
            break
        response, new_response_id = get_chatbot_response(user_input, previous_response_id)
        print(f"Lumina: {response}")
        previous_response_id = new_response_id  # পরের বারের জন্য আইডি সেভ করো

if __name__ == "__main__":
    main()