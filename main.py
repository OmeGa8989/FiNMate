import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configure the Gemini API with the key from the environment variable
try:
    # Corrected the environment variable name to match the error message
    genai.configure(api_key=os.getenv("API_KEY"))
except AttributeError:
    print("Error: The GOOGLE_API_KEY environment variable is not set.")
    print("Please create a .env file and add your API key.")
    exit()

# Initialize the generative model with a valid model name
model = genai.GenerativeModel('gemini-2.5-flash')


# --- MODIFICATION START ---
# Updated the hidden prompt to restrict the chatbot's scope.
initial_history = [
    {
        "role": "user",
        # This is the hidden instruction for the model
        "parts": [
            "System Instruction: Your expertise is strictly limited to finance and advisory topics. "
            "Your answers must be crisp and short. Do not answer questions or engage in conversations "
            "about any other subject. If a user asks about a topic outside of finance or advisory, "
            "you must politely decline and state that you can only discuss financial matters."
        ]
    },
    {
        "role": "model",
        # The model's acknowledgment of the instruction
        "parts": ["Understood. I will only answer questions about finance and advisory, and I will keep my answers concise."]
    }
]

# Start a chat session with the prepopulated history
chat = model.start_chat(history=initial_history)
# --- MODIFICATION END ---


def main():
    """
    The main function to run the chatbot.
    """
    print("🤖 Finance Chatbot is ready! (Type 'quit' or 'exit' to end the chat)")
    print("-" * 30)

    while True:
        # Get user input from the console
        user_input = input("You: ").strip()

        # Check for exit commands
        if user_input.lower() in ["quit", "exit"]:
            print("\n👋 Goodbye! Thanks for chatting.")
            break

        # Send the user's message to the model and get the response
        try:
            response = chat.send_message(user_input)
            # Print the model's response
            print(f"Gemini: {response.text}\n")
        except Exception as e:
            print(f"An error occurred: {e}")
            break

if __name__ == "__main__":
    main()