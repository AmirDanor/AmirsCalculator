from Validator import SET_VALID_CHARACTERS_IN_INPUT

class InvalidInputException(Exception):
    def __init__(self, string):
        """
        :param string: User input which caused the exception to be thrown
        :type string: str
        """
        self._string = string
    def __str__(self):
        """
        :return: Detailed message about the forbidden chars used in users input
        :rtype: str
        """
        forbidden_chars_from_string = {char for char in self._string if char not in SET_VALID_CHARACTERS_IN_INPUT}
        return 'Error! Your input contains forbidden characters: ' + str(forbidden_chars_from_string)