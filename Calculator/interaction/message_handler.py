from abc import ABC, abstractmethod

class MessageHandler(ABC):
    """
    Abstract class for displaying messages to user.
    """
    @abstractmethod
    def display_input_message(self):
        """
        Displays a message before user enters input.
        """
        pass

    @abstractmethod
    def display_custom_message(self, message:str):
        """
        Displays a custom message.
        :param message: Custom message to display
        :type message: str
        """
        pass

    @abstractmethod
    def display_error_message(self, error_message:str):
        """
        Displays an error message.
        :param error_message: Error message to display
        :type error_message: str
        """
        pass


MESSAGE_TO_DISPLAY = { # TODO: use something like colorama to color console text..
    0: '''
        \033[92m
                Welcome to Amir's Advanced Calculator!
                        This program simulates an improved calculator, which means it supports a wide range of operations, including:
                            •  Basic arithmetic (includes unary minus): +, -, *, /.
                            •  Advanced functions: sum (#), factorial (!), modulo (%), negation (~), minimum ($), maximum (&), and average (@).
                            •  All unary operators should be used as follows: unary minus [-operand], sum [operand#], factorial [operand!], and negation [~operand].
                            •  The rest of the operators are binary. Every binary operator should be placed between two operands.
                        Make sure to follow the rules when inserting mathematical expressions:
                            •  The only valid form of brackets is () (Parentheses / Round Brackets).
                            •  Use negation correctly by placing ~ (Tilda) directly before a number.
                        To stop the program from running, simply type "quit".
                        Start calculating by typing a mathematical expression below, then press enter to send input to program.
                        Enjoy! :)
        \033[00m
        ''',
    1: 'Please enter an input:'
}

class ConsoleMessageHandler(MessageHandler):
    """
    Class responsible for displaying console messages to user before entering an input.
    """
    def __init__(self):
        """
        Initialize the first message when creating a new instance of MessageHandler class.
        """
        self._prompt = MESSAGE_TO_DISPLAY[0]

    def display_input_message(self):
        """
        Displays a console message before user enters input
        (changes the text after the creation of the class
        which means - for the first time, the output is different).
        """
        print(self._prompt)
        if self._prompt != MESSAGE_TO_DISPLAY[1]:
            self._prompt = MESSAGE_TO_DISPLAY[1]

    def display_custom_message(self, message: str):
        """
        Displays a custom message in console.
        :param message: Custom message to display
        :type message: str
        """
        print(message)

    def display_error_message(self, error_message: str):
        """
        Displays an error message in console.
        :param error_message: Error message to display
        :type error_message: str
        """
        print(error_message)