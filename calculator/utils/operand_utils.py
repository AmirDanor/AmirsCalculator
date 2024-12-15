# Constants
from calculator.logic.operator_registry import OperatorRegistry # temp implementation. TODO: delete later to avoid high coupling.

VALID_INPUT_CHARACTERS = ({str(i) for i in range(10)} # int numbers 0 - 9 as str
                                 .union({ '+',
                                          '-',
                                          '*',
                                          '/',
                                          '^',
                                          '%',
                                          '$',
                                          '&',
                                          '@',
                                          '~',
                                          '!',
                                          '#',
                                          '(',
                                          ')',
                                          '.',
                                          ' ',
                                          '\t'})
                          )
SIGN_NUMBER_MINUS = '_'

SIGN_UNARY_MINUS = ';'

# Methods
def is_operand(string: str) -> bool:
    """
    Checks if string is operand
    :param string: string to check
    :type string: str
    :return: True if string is operand, else return False
    :rtype: bool
    """
    return string.isdigit() or '.' in string

def precedence(operator):
    """
    Gets operand's precedence
    :param operator: representation of operator
    :type operator: str
    :return: operator's precedence
    :rtype: int
    """
    return OperatorRegistry().get_precedence_for_operator(operator) # temp implementation. TODO: delete later to avoid high coupling.