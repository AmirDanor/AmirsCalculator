"""
Module for user input handling.
Contains an abstract base class and a console-specific implementation.
"""

from abc import ABC, abstractmethod


class InputHandler(ABC):
    """
    Abstract base class for obtaining input from user.
    """

    @abstractmethod
    def get_input(self):
        """
        Method to get input from the user.
        """

        pass


class ConsoleInputHandler(InputHandler):
    """
    Concrete class responsible for obtaining input from user through console.
    """

    def get_input(self) -> str:
        """
        Get input from user through console.

        :return: user input
        :rtype: str
        """

        return input()
