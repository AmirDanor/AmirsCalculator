from abc import ABC, abstractmethod

class InputHandler(ABC):
    """
    Abstract class for getting input from user
    """
    @abstractmethod
    def get_input(self):
        """
        Method to get input from the user.
        """
        pass

class ConsoleInputHandler(InputHandler):
    """
    Class responsible for getting input from user through console.
    """
    def get_input(self):
        """
        Get input from user through console
        :return: user input
        """
        return input()