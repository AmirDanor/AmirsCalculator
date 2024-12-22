"""
Main module for running the calculator application.

This module initializes and runs the calculator core, setting up the necessary
components for user interaction, message handling, tokenization, and token processing.
It utilizes the following modules:
- Console-based input and message handlers for user interaction.
- Arithmetic tokenizer and token processor for handling mathematical expressions.

Modules initialized:
- ConsoleMessageHandler: Handles messages displayed to the user through the console.
- ConsoleInputHandler: Handles input collection from the user through the console.
- ArithmeticTokenizer: Tokenizes mathematical expressions.
- ArithmeticTokenProcessor: Processes the arithmetic tokenized list.

The main function is executed when the module is run as the main program.
"""

from calculator.calculator_core import CalculatorCore
from calculator.interaction.input_handler import ConsoleInputHandler
from calculator.interaction.message_handler import ConsoleMessageHandler
from calculator.logic.string_preprocessor import ArithmeticStringPreprocessor
from calculator.logic.string_processor import ArithmeticStringProcessor
from calculator.logic.token_processor import ArithmeticTokenProcessor
from calculator.logic.tokenizer import ArithmeticTokenizer

if __name__ == "__main__":
    calculator_core = CalculatorCore(
        message_handler=ConsoleMessageHandler(),
        input_handler=ConsoleInputHandler(),
        string_preprocessor=ArithmeticStringPreprocessor(),
        string_processor=ArithmeticStringProcessor(),
        tokenizer=ArithmeticTokenizer(),
        token_processor=ArithmeticTokenProcessor()
    )
    calculator_core.run()
