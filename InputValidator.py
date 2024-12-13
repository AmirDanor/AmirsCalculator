from OperatorsFactory import OperatorFactory

operator_factory = OperatorFactory()
SET_VALID_CHARACTERS_IN_INPUT = ({str(i) for i in range(10)}
                                 .union({ '(', ')', '.', ' ', '\t'})
                                 .union(operator_factory.get_all_operator_symbols()))
SET_VALID_CHARACTERS_IN_INPUT.remove(';') # ; is not an actual character which user is allowed to enter...

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