# File contains prints for dev tests

from Calculator.interaction import input_handler, message_handler
from Calculator.interaction.input_handler import ConsoleInputHandler
from Calculator.interaction.message_handler import ConsoleMessageHandler
from Calculator.logic import input_validator
from Calculator.logic.exceptions import InvalidInputException
from Calculator.logic.equation_solver import EquationSolver
from Calculator.logic.string_formatter import StringFormatter

QUIT_STR = 'quit' # string which user has to enter to end program.
QUIT_MSG = 'Program Ended.' # string which get displayed to user after program ends.


class Main:
    """
    Class responsible for calling other functions from other classes.
    """
    def __init__(self, message_handler: message_handler.MessageHandler, input_handler: input_handler.InputHandler):
        """
        :param message_handler: An instance of the MessageHandler class to display prompts and messages
        :type message_handler: message_handler
        :param input_handler: An instance of the InputHandler class to get user input
        :type input_handler: input_handler
        """
        self.message_handler = message_handler
        self.input_handler = input_handler
        self.input_validator = input_validator.InputValidator()

    def run(self):
        """
        Runs the program as intended.
        :raises InvalidInputException: If user's input contains forbidden chars.
        """
        self.message_handler.display_input_message()
        try:
            expression = self.input_handler.get_input()
            while expression != QUIT_STR:
                try:
                    if not self.input_validator.validate_input(expression):
                        raise InvalidInputException(expression)
                except InvalidInputException as iie:
                    self.message_handler.display_custom_message(iie)  # Catch and print the InvalidInput exception
                else:
                    string_formatter = StringFormatter(expression)
                    expression = string_formatter.fix_format()
                    equation_solver = EquationSolver(expression)
                    self.message_handler.display_custom_message(equation_solver.solve())
                self.message_handler.display_input_message()
                expression = self.input_handler.get_input()
            self.message_handler.display_error_message(QUIT_MSG)
        except KeyboardInterrupt as kie:
            print("\nProgram Ended")

if __name__ == "__main__":
    main = Main(
        message_handler = ConsoleMessageHandler(),
        input_handler = ConsoleInputHandler(),
    )
    main.run()