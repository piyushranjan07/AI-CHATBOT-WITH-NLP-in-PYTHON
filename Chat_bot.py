#import necessary libraries
import nltk
import re

# Download NLTK data
nltk.download('punkt')

# Pattern-response pairs (all lowercase for consistency)
chat_patterns = {
    "hi|hello|hey": "Hello! How can I help you?",
    "how are you": "I'm just a bot, but I'm doing great!",
    "who are you|your name": "I'm your internship chatbot built using Python.",
    "thank you|thanks|thankyou": "You're welcome!",
    "bye|exit|quit": "Goodbye! Have a great day!",
    "what is python": "Python is a popular programming language used for AI, web, and automation.",
    "what is nltk": "NLTK is a Natural Language Processing library in Python.",
    "what is ai": "AI stands for Artificial Intelligence. It's about making machines think like humans.",
    "what is ml": "ML stands for Machine Learning. It's a way for computers to learn from data.",
    "what is data science": "Data science involves analyzing data to extract meaningful insights.",
    "uses of python": "Python is used in web development, data analysis, AI, scripting, and more.",
    "what is chatbot": "A chatbot is a computer program designed to simulate conversation with humans.",
    "what is internship": "An internship is a short-term opportunity to gain experience in a field.",
    "what is codtech": "CODTECH is your internship provider focused on building coding skills.",
    "who developed python": "Python was created by Guido van Rossum in 1991.",
    "what is function in python": "A function is a reusable block of code that performs a specific task.",
    "what is list in python": "A list is a collection of items stored in a single variable.",
    "what is loop in python": "Loops help you repeat tasks in code (like for, while).",
    "what is variable": "A variable is used to store information to be referenced and manipulated.",
    "what is ide": "IDE stands for Integrated Development Environment, like VS Code or PyCharm.",
    "what is vs code": "VS Code is a popular code editor developed by Microsoft.",
    "what is html": "HTML stands for HyperText Markup Language. It's used to create web pages.",
    "what is css": "CSS is used to style HTML content — for color, layout, and fonts.",
    "what is javascript": "JavaScript is a scripting language used to create interactive web content.",
    "yes|okay|sure": "Great! What would you like to learn about?"
}

# Function to generate response
def get_response(user_input):
    user_input = user_input.lower()
    for pattern, response in chat_patterns.items():
        if re.search(pattern, user_input):
            return response
    return "Sorry, I didn't understand that. Please try asking something else."

# Start chatbot
print("BOT: Hello! I’m your chatbot. Type 'bye' to exit.")

while True:
    user_input = input("YOU: ")
    if re.search(r"bye|exit|quit", user_input.lower()):
        print("BOT:", chat_patterns["bye|exit|quit"])
        break
    print("BOT:", get_response(user_input))
