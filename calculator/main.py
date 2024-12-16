# File contains prints for dev tests

from calculator.interaction import input_handler, message_handler
from calculator.interaction.input_handler import ConsoleInputHandler
from calculator.interaction.message_handler import ConsoleMessageHandler
from calculator.logic import input_validator, token_processor
from calculator.logic.exceptions import InvalidInputError, UnaryError, EmptyParenthesesError
from calculator.logic.equation_solver import EquationSolver
from calculator.logic.string_formatter import StringFormatter
from calculator.logic.token_processor import ArithmeticTokenProcessor, TokenProcessor
from calculator.logic.tokenizer import Tokenizer, ArithmeticTokenizer

QUIT_STR = 'quit' # string which user has to enter to end program.
QUIT_MSG = 'Program Ended.' # string which get displayed to user after program ends.


class Main:
    """
    Class responsible for calling other functions from other classes.
    """
    def __init__(self, message_handler: message_handler.MessageHandler, input_handler: input_handler.InputHandler, tokenizer: Tokenizer, token_processor: TokenProcessor):
        """
        :param message_handler: An instance of the MessageHandler class to display prompts and messages
        :type message_handler: message_handler
        :param input_handler: An instance of the InputHandler class to get user input
        :type input_handler: input_handler
        """
        self.message_handler = message_handler
        self.input_handler = input_handler
        self.input_validator = input_validator.InputValidator()
        self.tokenizer = tokenizer
        self.token_processor = token_processor

    def run(self):
        """
        Runs the program as intended.
        :raises InvalidInputError: If user's input contains forbidden chars.
        """
        self.message_handler.display_input_message()
        try:
            expression = self.input_handler.get_input()
            while expression != QUIT_STR:
                try:
                    if not self.input_validator.validate_input(expression):
                        raise InvalidInputError(expression)
                except InvalidInputError as iie:
                    self.message_handler.display_custom_message(str(iie))  # Catch and print the InvalidInput exception
                else:
                    try:
                        string_formatter = StringFormatter(expression)
                        expression = string_formatter.fix_format()
                        tokenized_equation = self.tokenizer.tokenize(expression)
                        processed_tokenized_equation = self.token_processor.process(tokenized_equation)
                        #print(self.token_processor.validate())
                        equation_solver = EquationSolver(processed_tokenized_equation)
                        solution = equation_solver.solve()
                        if solution is not None: # if solution is not None
                            self.message_handler.display_custom_message(str(solution))
                    except EmptyParenthesesError as epe:
                        self.message_handler.display_error_message(epe) # TODO: change text displayed
                    except UnaryError as ue:
                        self.message_handler.display_error_message(ue)  # TODO: change text displayed
                    except IndexError as ie:
                        self.message_handler.display_error_message('Error: Missing operands') # TODO: change text displayed
                        # triggered by (((6)
                self.message_handler.display_input_message()
                expression = self.input_handler.get_input()
            self.message_handler.display_error_message(QUIT_MSG)
        except KeyboardInterrupt as kie:
            self.message_handler.display_error_message("\nProgram Ended")

if __name__ == "__main__":
    main = Main(
        message_handler = ConsoleMessageHandler(QUIT_STR),
        input_handler = ConsoleInputHandler(),
        tokenizer = ArithmeticTokenizer(),
        token_processor = ArithmeticTokenProcessor()
    )
    main.run()