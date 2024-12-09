from InputValidator import SET_VALID_CHARACTERS_IN_INPUT

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
        forbidden_chars_from_string = {char for char in self._string if char not in SET_VALID_CHARACTERS_IN_INPUT}
        return f'Error! Your input contains forbidden characters: {forbidden_chars_from_string}'
