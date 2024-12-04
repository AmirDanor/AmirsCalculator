import InputHandler
from ConsoleInputHandler import ConsoleInputHandler
import MessageHandler
from ConsoleMessageHandler import ConsoleMessageHandler
import Validator
from Exceptions import InvalidInputException

QUIT_STR = 'quit' # string which user has to enter to end program.
QUIT_MSG = 'Program Ended.' # string which get displayed to user after program ends.


class Main:
    """
    Class responsible for calling other functions from other classes.
    """
    def __init__(self, message_handler: MessageHandler, input_handler: InputHandler, input_validator: Validator):
        """
        :param message_handler: An instance of the MessageHandler class to display prompts and messages
        :type message_handler: MessageHandler
        :param input_handler: An instance of the InputHandler class to get user input
        :type input_handler: InputHandler
        :param input_validator: An instance of the InputValidator class to validate user input
        :type input_validator: InputValidator
        """
        self.message_handler = message_handler
        self.input_handler = input_handler
        self.input_validator = input_validator
    def run(self):
        """
        Runs the program as intended.
        :raises InvalidInputException: If user's input contains forbidden chars.
        """
        self.message_handler.display_input_message()
        expression = self.input_handler.get_input()
        while expression != QUIT_STR:
            try:
                if not self.input_validator.validate_input(expression):
                    raise InvalidInputException(expression)
            except InvalidInputException as iie:
                self.message_handler.display_custom_message(iie)  # Catch and print the InvalidInput exception
            self.message_handler.display_input_message()
            expression = self.input_handler.get_input()
        self.message_handler.display_error_message(QUIT_MSG)

if __name__ == "__main__":
    main = Main(
        message_handler = ConsoleMessageHandler(),
        input_handler = ConsoleInputHandler(),
        input_validator = Validator.InputValidator()
    )
    main.run()