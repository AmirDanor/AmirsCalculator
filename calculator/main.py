from calculator.calculator_core import QUIT_STR, CalculatorCore
from calculator.interaction.input_handler import ConsoleInputHandler
from calculator.interaction.message_handler import ConsoleMessageHandler
from calculator.logic.token_processor import ArithmeticTokenProcessor
from calculator.logic.tokenizer import ArithmeticTokenizer

if __name__ == "__main__":
    calculator_core = CalculatorCore(
        message_handler=ConsoleMessageHandler(QUIT_STR),
        input_handler=ConsoleInputHandler(),
        tokenizer=ArithmeticTokenizer(),
        token_processor=ArithmeticTokenProcessor()
    )
    calculator_core.run()
