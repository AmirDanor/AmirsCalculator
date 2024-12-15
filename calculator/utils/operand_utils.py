# Constants
from calculator.utils.operator_registry import OperatorRegistry # temp implementation. TODO: delete later to avoid high coupling.

operator_registry = OperatorRegistry() #todo: change ??? because its a var in module...

SIGN_NUMBER_MINUS = '_'

SIGN_UNARY_MINUS = ';'

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

ALLOWED_BEFORE_RIGHT_UNARY = ({str(i) for i in range(10)} # int numbers 0 - 9 as str
                                 .union({ ')', '!', '#'}) #TODO: link with actual set. make it more modular
                          )
ALLOWED_AFTER_RIGHT_UNARY = (set(operator_registry.get_right_unary_operators())
                             .union(operator_registry.get_binary_operators())
                             .union({')'}))


# Methods
def is_operand(string: str) -> bool:
    """
    Checks if string is operand
    :param string: string to check
    :type string: str
    :return: True if string is operand, else return False
    :rtype: bool
    """
    return string.isdigit() or '.' in string or '_' in string

def precedence(operator):
    """
    Gets operand's precedence
    :param operator: representation of operator
    :type operator: str
    :return: operator's precedence
    :rtype: int
    """
    return OperatorRegistry().get_precedence_for_operator(operator) # temp implementation. TODO: delete later to avoid high coupling.