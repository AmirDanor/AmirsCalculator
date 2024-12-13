import ValidCharacters
from ValidCharacters import VALID_INPUT_CHARACTERS


class InvalidInputException(Exception):
    def __init__(self, string):
        """
        :param string: User input which caused the exception
        :type string: str
        """
        self._string = string
    def __str__(self):
        """
        :return: Detailed message about the forbidden chars used in users input
        :rtype: str
        """
        forbidden_chars_from_string = {char for char in self._string if char not in VALID_INPUT_CHARACTERS}
        return f'Error! Your input contains forbidden characters: {forbidden_chars_from_string}'

class NegativeFactorial(Exception):
    def init(self, number):
        """
        :param number: Negative number which raised the exception
        :type number: float
        """
        self._number = number
    def str(self):
        """
        :return: Message about the cause of the exception
        :rtype: str
        """
        return f'Error! Cannot calculate factorial for negative number: {self._number}'