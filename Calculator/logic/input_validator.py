from Calculator.logic import valid_characters

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
        return set(expression).issubset(valid_characters.VALID_INPUT_CHARACTERS)