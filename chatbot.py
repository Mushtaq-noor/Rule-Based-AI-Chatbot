"""
Rule-Based AI Chatbot
Author: Mushtaq Noor

A command-line chatbot that uses text preprocessing, regular-expression
intent matching, and predefined responses. Uses only Python's standard library.
"""

import re
from typing import Dict, Pattern


# Exit commands must match the entire cleaned message.
EXIT_PATTERN = re.compile(r"^(?:bye|goodbye|exit|quit|see you later)$")

# Order matters: more specific intents should be checked before broad ones.
INTENT_PATTERNS: Dict[str, Pattern[str]] = {
    "creator": re.compile(r"\b(?:who created you|who made you)\b"),
    "data_science": re.compile(r"\bdata science\b"),
    "status": re.compile(r"\bhow are you\b"),
    "greeting": re.compile(r"\b(?:hello|hi|hey)\b"),
    "thanks": re.compile(r"\b(?:thank you|thanks)\b"),
    "weather": re.compile(r"\bweather\b"),
    "joke": re.compile(r"\bjoke\b"),
    "help": re.compile(r"\bhelp\b"),
    "python": re.compile(r"\bpython\b"),
    "ai": re.compile(r"\b(?:ai|artificial intelligence)\b"),
}

RESPONSES: Dict[str, str] = {
    "creator": "I was created by Mushtaq Noor using Python.",
    "data_science": (
        "Data Science combines programming, statistics, and domain "
        "knowledge to extract useful insights from data."
    ),
    "status": "I am doing great! Thanks for asking.",
    "greeting": "Hello! How can I help you?",
    "thanks": "You're welcome! Happy to help.",
    "weather": "I cannot check live weather yet.",
    "joke": (
        "Why do programmers prefer dark mode? "
        "Because light attracts bugs!"
    ),
    "help": (
        "You can ask me about Python, AI, Data Science, the weather, "
        "jokes, or say hello. Type 'bye' to exit."
    ),
    "python": "Python is a popular, general-purpose programming language.",
    "ai": "AI stands for Artificial Intelligence.",
    "empty": "Please enter a message.",
    "unknown": (
        "Sorry, I don't understand that yet. "
        "Type 'help' to see what I can answer."
    ),
}


def preprocess_text(message: str) -> str:
    """Normalize a message by lowercasing, trimming, and removing punctuation."""
    if not isinstance(message, str):
        raise TypeError("message must be a string")

    normalized = message.lower().strip()
    normalized = re.sub(r"[^\w\s]", " ", normalized)
    normalized = re.sub(r"\s+", " ", normalized).strip()
    return normalized


def recognize_intent(message: str) -> str:
    """Return the intent associated with a user message."""
    cleaned_message = preprocess_text(message)

    if not cleaned_message:
        return "empty"

    if EXIT_PATTERN.fullmatch(cleaned_message):
        return "exit"

    for intent, pattern in INTENT_PATTERNS.items():
        if pattern.search(cleaned_message):
            return intent

    return "unknown"


def generate_response(intent: str) -> str:
    """Return a predefined response for an intent."""
    if intent == "exit":
        return "Goodbye! Have a great day!"

    return RESPONSES.get(intent, RESPONSES["unknown"])


def get_response(message: str) -> str:
    """Process a message from input to final chatbot response."""
    intent = recognize_intent(message)
    return generate_response(intent)


def run_chatbot() -> None:
    """Run the chatbot in an interactive command-line loop."""
    print("=" * 50)
    print("             RULE-BASED AI CHATBOT")
    print("             Developed by Mushtaq Noor")
    print("=" * 50)
    print("Chatbot: Hello! Type 'help' for topics or 'bye' to exit.")

    while True:
        try:
            user_message = input("\nYou: ")
            intent = recognize_intent(user_message)
            response = generate_response(intent)
            print(f"Chatbot: {response}")

            if intent == "exit":
                break

        except (KeyboardInterrupt, EOFError):
            print("\nChatbot: Session ended. Goodbye!")
            break


if __name__ == "__main__":
    run_chatbot()
