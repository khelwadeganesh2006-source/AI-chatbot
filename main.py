
import re
import random
from datetime import datetime


# ---------------- CHATBOT CONFIGURATION ----------------

BOT_NAME = "RuleBot"

RULES = [
    (
        r"\b(hi|hello|hey|hiya)\b",
        [
            "Hello! How can I help you?",
            "Hi there! Nice to meet you.",
            "Hey! What would you like to talk about?"
        ]
    ),
    (
        r"\b(good morning)\b",
        ["Good morning! Have a wonderful day."]
    ),
    (
        r"\b(good afternoon)\b",
        ["Good afternoon! How can I assist you?"]
    ),
    (
        r"\b(good evening)\b",
        ["Good evening! What can I do for you?"]
    ),
    (
        r"\bhow are you\b",
        [
            "I'm doing great! Thanks for asking.",
            "I'm fine and ready to chat with you."
        ]
    ),
    (
        r"\b(your name|who are you|what are you)\b",
        [
            "I'm RuleBot, a simple rule-based chatbot built with Python."
        ]
    ),
    (
        r"\bwhat can you do\b|\bhelp\b",
        [
            "I can respond to greetings, answer basic questions, "
            "tell you the date and time, and chat using predefined rules."
        ]
    ),
    (
        r"\b(time|current time)\b",
        [f"The current time is {datetime.now().strftime('%I:%M:%S %p')}."]
    ),
    (
        r"\b(date|today's date|current date)\b",
        [f"Today's date is {datetime.now().strftime('%d %B %Y')}."]
    ),
    (
        r"\bhow is the weather\b|\bweather\b",
        [
            "I cannot check live weather, but you can use a weather app "
            "to get the latest forecast."
        ]
    ),
    (
        r"\bwhat is python\b|\bdefine python\b",
        [
            "Python is a popular programming language used in web "
            "development, automation, data science, and AI."
        ]
    ),
    (
        r"\bwhat is ai\b|\bartificial intelligence\b",
        [
            "Artificial Intelligence (AI) enables computers to perform "
            "tasks that typically require human intelligence."
        ]
    ),
    (
        r"\bthank you\b|\bthanks\b",
        [
            "You're welcome!",
            "Happy to help!",
            "Anytime! Let me know if you need anything else."
        ]
    ),
    (
        r"\bhow are things\b|\bhow is it going\b",
        ["Everything is going well here! How about you?"]
    ),
    (
        r"\b(bye|goodbye|see you|exit|quit)\b",
        ["Goodbye! Thanks for chatting with me. Have a great day!"]
    )
]


# ---------------- RESPONSE ENGINE ----------------

def get_response(user_input):
    """Return a response based on predefined keyword patterns."""

    message = user_input.lower().strip()
    message = re.sub(r"\s+", " ", message)

    if not message:
        return "Please type a message so I can respond."

    for pattern, responses in RULES:
        if re.search(pattern, message):
            # Update the time/date when requested.
            if re.search(r"\b(time|current time)\b", message):
                return (
                    "The current time is "
                    + datetime.now().strftime("%I:%M:%S %p")
                    + "."
                )

            if re.search(
                r"\b(date|today's date|current date)\b", message
            ):
                return (
                    "Today's date is "
                    + datetime.now().strftime("%d %B %Y")
                    + "."
                )

            return random.choice(responses)

    return (
        "I'm not sure how to answer that yet. "
        "Try saying 'hello', asking 'what is Python?', "
        "or typing 'help' to see what I can do."
    )


# ---------------- CHAT INTERFACE ----------------

def display_welcome():
    print("=" * 50)
    print(f"          Welcome to {BOT_NAME}!")
    print("       Your Rule-Based Chatbot")
    print("=" * 50)
    print("Type 'help' to learn what I can do.")
    print("Type 'bye' or 'exit' to end the conversation.")
    print("-" * 50)


def chat():
    display_welcome()

    while True:
        try:
            user_input = input("You: ").strip()
        except (KeyboardInterrupt, EOFError):
            print(f"\n{BOT_NAME}: Goodbye! Thanks for chatting.")
            break

        if not user_input:
            print(f"{BOT_NAME}: Please type a message.")
            continue

        response = get_response(user_input)
        print(f"{BOT_NAME}: {response}")

        # Exit only when the complete input is an exit command.
        if user_input.lower().strip() in {
            "bye", "goodbye", "see you", "exit", "quit"
        }:
            break

    print("Chat session ended.")


# ---------------- START APPLICATION ----------------

if __name__ == "__main__":
    chat()
