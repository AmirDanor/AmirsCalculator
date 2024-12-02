from abc import ABC, abstractmethod

class MessageHandler(ABC):
    """
    Abstract class for displaying messages to user
    """
    @abstractmethod
    def display_message(self):
        pass

    @abstractmethod
    def display_custom_message(self, message:str):
        pass

    @abstractmethod
    def display_error_message(self, error_message:str):
        pass