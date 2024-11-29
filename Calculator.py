SET_VALID_CHARACTERS_IN_INPUT = {
    '0', '1', '2',
    '3', '4', '5',
    '6', '7', '8',
    '9', '+', '-',
    '*', '/', '^',
    '@', '$', '&',
    '%', '~', '!',
    '(', ')', '.',
    ' ', '\t'
}

class MessageHandler:
    """
    This class is responsible for displaying messages to user before entering an input.
    """
    def __init__(self):
        """
        This function is responsible for initializing the first message when creating a new instance of MessageHandler class.

        Attributes:
            _prompt (str): A message for the user.
        """
        self._prompt = '''
                Welcome to Amir's Advanced Calculator!
                        This program simulates an improved calculator, which means it supports a wide range of operations, including:
                            •  Basic arithmetic: +, -, *, /.
                            •  Advanced functions: factorial (!), modulo (%), negation (~), minimum ($), maximum (&), and average (@).
                        Make sure to follow the rules when inserting mathematical expressions:
                            •  The only valid form of brackets is () (Parentheses / Round Brackets).
                            •  Use negation correctly by placing ~ (Tilda) directly before a number.
                        To stop the program from running, simply type "quit".
                        Start calculating by typing a mathematical expression below, then press enter to send input to program. Enjoy!
                        '''

    def print_message_before_input(self):
        """
        This function is responsible for printing a message before user enters input.
        It also changes the text after the creation of the class (for the first time, the output is different).
        """
        print(self._prompt)
        if self._prompt != 'Please enter an input:':
            self._prompt = 'Please enter an input:'

class InputHandler:
    """
    This class is responsible for getting input from user.
    """
    def get_input(self):
        """
        Returns:
            This function returns the users input.
        """
        return input()


class InputValidator:
    """
    This class is responsible for validating input user entered.
    """
    def validate_input(self, expression: str) -> bool:
        """
        This function checks if there are forbidden chars in the user input.

        Args:
            expression (str): The string which needed to get validated.

        Returns:
            bool: The expression doesn't contain forbidden chars. True fore does not, False for does.
        """
        return set(expression).issubset(SET_VALID_CHARACTERS_IN_INPUT)

class InvalidInputException(Exception):
    def __init__(self, string):
        """
        Args:
            string (str): String which caused the exception to be thrown.

        Attributes:
            _string (str): String which caused the exception to be thrown.
        """
        self._string = string
    def __str__(self):
        """
        Returns:
             str: Detailed message about the forbidden chars used in users input.
        """
        forbidden_chars_from_string = {char for char in self._string if char not in SET_VALID_CHARACTERS_IN_INPUT}
        return 'Error! Your input contains forbidden characters: ' + str(forbidden_chars_from_string)

class Calculator:
    """
    This class is mainly responsible for calling other functions from other classes.
    """
    def __init__(self, message_handler, input_handler, input_validator):
        """
        Args + Attributes:
            message_handler (MessageHandler): An instance of the MessageHandler class to display prompts and messages.
            input_handler (InputHandler): An instance of the InputHandler class to get user input.
            input_validator (InputValidator): An instance of the InputValidator class to validate user input.
        """
        self.message_handler = message_handler
        self.input_handler = input_handler
        self.input_validator = input_validator

    def run(self):
        """
        Attributes:
            expression (str): User's input.
            iie (InvalidInputException): Exception for inserting forbidden chars.
        Raises:
            InvalidInputException:  When user's input contains forbidden chars.
        """
        self.message_handler.print_message_before_input()
        expression = self.input_handler.get_input()
        while expression != 'quit':
            try:
                if not self.input_validator.validate_input(expression):
                    raise InvalidInputException(expression)
            except InvalidInputException as iie:
                print(iie)  # Catch and print the InvalidInput exception
            self.message_handler.print_message_before_input()
            expression = self.input_handler.get_input()
        print("Program Stopped.")

"""
Used to run program correctly.
"""
if __name__ == "__main__":
    calculator = Calculator(
        message_handler = MessageHandler(),
        input_handler = InputHandler(),
        input_validator = InputValidator()
    )
    calculator.run()