# Rule-Based AI Chatbot

import random

GREETING_RESPONSES = [
    "Hello! How can I help you today?",
    "Hey there! What's up?",
    "Hi! Good to see you.",
    "Hello again! What can I do for you?",
]


def chatbot():
    print("🤖 Hello! I'm ChatBot. Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower().strip()

        if user_input in ["hi", "hello", "hey"]:
            print("Bot:", random.choice(GREETING_RESPONSES))
        elif user_input in ["bye", "exit", "quit"]:
            print("Bot: Goodbye! Have a great day! 👋")
            break
        elif "how are you" in user_input:
            print("Bot: I am doing well, thanks for asking!")
        elif "your name" in user_input:
            print("Bot: I'm ChatBot, your friendly rule-based assistant.")
        elif "help" in user_input:
            print("Bot: I can respond to greetings, tell you my name, or say bye when you're done.")
        elif user_input == "":
            print("Bot: Please type something.")
        else:
            print("Bot: Sorry, I didn't understand that. Try saying 'hi' or 'help'.")


if __name__ == "__main__":
    chatbot()
