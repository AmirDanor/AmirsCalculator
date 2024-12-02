SET_VALID_CHARACTERS_IN_INPUT = {
    '0', '1', '2',
    '3', '4', '5',
    '6', '7', '8',
    '9', '+', '-',
    '*', '/', '^',
    '@', '$', '&',
    '%', '~', '!',
    '(', ')', '.',
    ' ', '\t'
}

class InputValidator:
    """
    Utility class responsible for validating user input for mathematical expressions.
    """

    @staticmethod
    def validate_input(expression: str) -> bool:
        """
        Checks if there are forbidden chars in the user input
        :param expression: Mathematical expression which needed to get validated
        :type expression: str
        :return: Whether expression contains forbidden chars or not
        :rtype: bool
        """
        return set(expression).issubset(SET_VALID_CHARACTERS_IN_INPUT)