import random

# Predefined responses for greetings, farewells, and questions
GREETING_INPUTS = ["hello", "hi", "hey", "greetings", "sup", "what's up"]
GREETING_RESPONSES = ["Hi there!", "Hello!", "Hey!", "Greetings!", "How can I help you?"]

FAREWELL_INPUTS = ["bye", "goodbye", "see you", "exit", "quit"]
FAREWELL_RESPONSES = ["Bye!", "Goodbye!", "See you later!", "Take care!"]

KNOWLEDGE_BASE = {
    "your name": "I'm a simple chatbot created in Python.",
    "how are you": "I'm just a bunch of code, but I'm doing great!",
    "what can you do": "I can chat with you and answer simple questions.",
    "python": "Python is a powerful, high-level programming language.",
    "nltk": "NLTK is a library for natural language processing in Python."
}

# Basic text matching
def check_greeting(user_input):
    for word in GREETING_INPUTS:
        if word in user_input.lower():
            return random.choice(GREETING_RESPONSES)
    return None

def check_farewell(user_input):
    for word in FAREWELL_INPUTS:
        if word in user_input.lower():
            return random.choice(FAREWELL_RESPONSES)
    return None

# Get response from knowledge base
def get_response(user_input):
    # Check for greeting
    greeting = check_greeting(user_input)
    if greeting:
        return greeting

    # Check for farewell
    farewell = check_farewell(user_input)
    if farewell:
        return farewell

    # Check if the input matches any question in the knowledge base
    for key, response in KNOWLEDGE_BASE.items():
        if key in user_input.lower():
            return response

    # Default response for unknown input
    return "Sorry, I don't understand that yet."

# Chat loop
def chat():
    print("Chatbot: Hello! Ask me something or say 'bye' to exit.")
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in FAREWELL_INPUTS:
            print(f"Chatbot: {random.choice(FAREWELL_RESPONSES)}")
            break
        response = get_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    chat()
