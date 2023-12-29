import re

def rule_based_chatbot(user_input):
    # Convert user input to lowercase for case-insensitivity
    user_input = user_input.lower()

    # Define rules and responses
    greeting_patterns = ['hello', 'hi', 'hey']
    goodbye_patterns = ['bye', 'goodbye']
    inquiry_patterns = ['how are you', 'what is your name', 'who are you']
    default_response = "I'm sorry, I don't understand. Can you please rephrase your question?"

    # Pattern matching for greetings
    if any(pattern in user_input for pattern in greeting_patterns):
        return "Hello! How can I help you today?"

    # Pattern matching for goodbyes
    elif any(pattern in user_input for pattern in goodbye_patterns):
        return "Goodbye! Have a great day!"

    # Pattern matching for inquiries
    elif any(pattern in user_input for pattern in inquiry_patterns):
        return "I am a chatbot designed to assist you. My name is ChatGPT."

    # Default response if no pattern is matched
    else:
        return default_response

# Example usage
user_input = input("User: ")
response = rule_based_chatbot(user_input)
print("Chatbot:", response)
