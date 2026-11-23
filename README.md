# Rule-Based AI Chatbot

A beginner-friendly Python command-line chatbot that recognizes predefined user intents and responds with rule-based logic. It demonstrates text preprocessing, regular expressions, modular functions, and automated unit testing.

**Developer:** Mushtaq Noor  
**Language:** Python 3  
**Dependencies:** Python standard library only

## Features

- Responds to greetings such as `hello`, `hi`, and `hey`.
- Recognizes common intents including status, creator, Python, AI, Data Science, weather, jokes, thanks, and help.
- Uses text preprocessing to normalize capitalization, punctuation, and whitespace.
- Uses regular expressions and word boundaries for more reliable keyword matching.
- Runs continuously until the user enters an exit command.
- Handles Ctrl+C and end-of-input interruptions gracefully.
- Includes automated tests using Python's built-in `unittest` framework.

## Project structure

```text
Rule-Based-AI-Chatbot/
├── chatbot.py
├── test_chatbot.py
├── README.md
├── requirements.txt
├── .gitignore
└── LICENSE
```

## Requirements

- Python 3.8 or newer
- No third-party packages are required.

## Run the chatbot

1. Clone the repository:

   ```bash
   git clone https://github.com/Mushtaq-noor/Rule-Based-AI-Chatbot.git
   ```

2. Move into the project directory:

   ```bash
   cd Rule-Based-AI-Chatbot
   ```

3. Start the chatbot:

   ```bash
   python chatbot.py
   ```

## Example conversation

```text
RULE-BASED AI CHATBOT
Chatbot: Hello! Type 'help' for topics or 'bye' to exit.

You: HELLO!
Chatbot: Hello! How can I help you?

You: Tell me about Data Science
Chatbot: Data Science combines programming, statistics, and domain knowledge to extract useful insights from data.

You: Tell me a joke
Chatbot: Why do programmers prefer dark mode? Because light attracts bugs!

You: bye
Chatbot: Goodbye! Have a great day!
```

## Run automated tests

From the project directory, run:

```bash
python -m unittest -v
```

The test suite checks text preprocessing, intent recognition, exit handling, response generation, and representative end-to-end behavior.

## How it works

1. **Preprocessing:** `preprocess_text()` lowercases the message, trims whitespace, removes punctuation, and normalizes repeated spaces.
2. **Intent recognition:** `recognize_intent()` compares the cleaned message against predefined regular-expression patterns.
3. **Response generation:** `generate_response()` selects a predefined response for the detected intent.
4. **Conversation loop:** `run_chatbot()` repeatedly accepts input until an exit command is recognized.

## Limitations

This is a rule-based demonstration, not a generative or machine-learning chatbot. It does not learn from conversations, understand context, or access live information. Messages that do not match its predefined patterns receive a fallback response.

## Future improvements

- Add more intents and response variations.
- Move intent patterns and responses into a configuration file.
- Add conversation context and logging.
- Build a simple web interface with Streamlit or Gradio.
- Explore machine-learning-based intent classification.

## License

This project is released under the MIT License. See [LICENSE](LICENSE) for details.
