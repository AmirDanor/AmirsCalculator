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