"""
Module for displaying messages to the user.
Contains an abstract base class and a console-specific implementation.
"""

from abc import ABC, abstractmethod

import colorama
from colorama import Fore, Back

from calculator.utils import general_utils


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
    def display_custom_message(self, message: str):
        """
        Displays a custom message.
        :param message: Custom message to display
        :type message: str
        """

        pass

    @abstractmethod
    def display_result_message(self, result_message: str):
        """
        Displays an equation result message.
        :param result_message: Result message to display
        :type result_message: str
        """

        pass

    @abstractmethod
    def display_error_message(self, error_message: str):
        """
        Displays an error message.
        :param error_message: Error message to display
        :type error_message: str
        """

        pass

    @abstractmethod
    def display_quit_message(self):
        """
        Displays an exit message when user quits program.
        """

        pass


class ConsoleMessageHandler(MessageHandler):
    """
    Class responsible for displaying console messages to user before
    entering an input.
    """

    def __init__(self):
        """
        Initialize the first message when creating a new instance of
        MessageHandler class.
        """

        colorama.init()  # Used for colored console text
        self._quit = general_utils.QUIT_STR

        self._message_to_display = {
            0: f'''         {Back.LIGHTWHITE_EX + Fore.RED}  Welcome to Amir's Advanced Calculator!  {Fore.LIGHTGREEN_EX + Back.RESET}
                        This program simulates an improved calculator, which
                        means it supports a wide range of operations, including:{Fore.LIGHTCYAN_EX}
                            •  Basic arithmetic (includes unary minus): +, -, *, /.
                            •  Advanced functions: sum (#), factorial (!),
                                modulo (%), negation (~), minimum ($),
                                maximum (&), and average (@).
                            •  All unary operators should be used as follows:
                                unary minus [-operand], sum [operand#],
                                factorial [operand!], and negation [~operand].
                            •  The rest of the operators are binary.
                                Every binary operator should be placed
                                between two operands.{Fore.LIGHTGREEN_EX}
                        Make sure to follow the rules when inserting mathematical expressions:{Fore.LIGHTCYAN_EX}
                            •  The only valid form of brackets is () (Parentheses / Round Brackets).
                            •  Use negation correctly by placing ~ (Tilde) directly before a number.{Fore.RED}
                        To stop the program from running, simply type "{self._quit}".{Fore.LIGHTMAGENTA_EX}
                        Start calculating by typing a mathematical expression below,
                        then press enter to send input to program.{Fore.LIGHTYELLOW_EX}
                        Enjoy! :){Fore.RESET}''',
            1: 'Please enter an input:'
        }
        self._prompt = self._message_to_display[0]

    def display_input_message(self):
        """
        Displays a console message before user enters input
        (changes the text after the creation of the class
        which means - for the first time, the output is different).
        """

        print(self._prompt)
        if self._prompt != self._message_to_display[1]:
            self._prompt = self._message_to_display[1]

    def display_custom_message(self, message: str):
        """
        Displays a custom message in console.

        :param message: Custom message to display
        :type message: str
        """

        print(message)

    def display_result_message(self, result_message: str):
        """
        Displays an equation result message in console.

        :param result_message: Result message to display.
        :type result_message: str
        """

        print(Fore.LIGHTGREEN_EX + result_message + Fore.RESET)

    def display_error_message(self, error_message: str):
        """
        Displays an error message in console.

        :param error_message: Error message to display.
        :type error_message: str
        """

        print(Fore.RED + error_message + Fore.RESET)

    def display_quit_message(self):
        """
        Displays a console exit message when program ends.
        """
        print(Fore.MAGENTA + "Program Ended." + Fore.RESET)
