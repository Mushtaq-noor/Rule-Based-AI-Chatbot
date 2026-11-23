"""Automated tests for the Rule-Based AI Chatbot."""

import unittest

from chatbot import (
    generate_response,
    get_response,
    preprocess_text,
    recognize_intent,
)


class TestTextPreprocessing(unittest.TestCase):
    def test_lowercase_and_punctuation(self):
        self.assertEqual(preprocess_text(" HELLO, Chatbot! "), "hello chatbot")

    def test_repeated_whitespace(self):
        self.assertEqual(preprocess_text("how   are    you"), "how are you")

    def test_empty_message(self):
        self.assertEqual(preprocess_text("   "), "")

    def test_non_string_input_raises_type_error(self):
        with self.assertRaises(TypeError):
            preprocess_text(None)


class TestIntentRecognition(unittest.TestCase):
    def test_known_intents(self):
        cases = [
            ("HELLO!", "greeting"),
            ("Hi there", "greeting"),
            ("This is interesting", "unknown"),
            ("How are you?", "status"),
            ("Who created you?", "creator"),
            ("Tell me about data science", "data_science"),
            ("Thank you so much", "thanks"),
            ("Tell me a joke", "joke"),
            ("I need help", "help"),
            ("What is Python?", "python"),
            ("What is AI?", "ai"),
            ("Can you tell me the weather?", "weather"),
            ("", "empty"),
            ("   ", "empty"),
            ("bye", "exit"),
            ("See you later!", "exit"),
        ]

        for message, expected_intent in cases:
            with self.subTest(message=message):
                self.assertEqual(
                    recognize_intent(message),
                    expected_intent,
                )

    def test_exit_requires_a_complete_command(self):
        self.assertEqual(recognize_intent("goodbye everyone"), "unknown")
        self.assertEqual(recognize_intent("I will not quit"), "unknown")


class TestResponseGeneration(unittest.TestCase):
    def test_exit_response(self):
        self.assertEqual(
            generate_response("exit"),
            "Goodbye! Have a great day!",
        )

    def test_unknown_intent_has_fallback(self):
        self.assertIn("don't understand", generate_response("not_a_real_intent"))

    def test_end_to_end_response(self):
        self.assertEqual(
            get_response("Thank you!"),
            "You're welcome! Happy to help.",
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
