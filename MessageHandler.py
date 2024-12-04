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