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


def get_all_operator_symbols(self):
    """
    Get all operators str symbol representation as set

    :return: all operator symbols
    :rtype: set
    """
    return (set(self._left_unary_operators_funcs.keys())
            .union(self._right_unary_operators_funcs.keys())
            .union(self._binary_operators_funcs.keys()))


def get_unary_operators(self):
    """
    Get all unary operators str symbol representation as set

    :return: all unary operator symbols
    :rtype: dict
    """
    merged_unaries_dict = {**self._left_unary_operators_funcs, **self._right_unary_operators_funcs}
    return merged_unaries_dict


def get_left_unary_operators(self):
    """
    Get all left unary operators str symbol representation as set

    :return: all left unary operator symbols
    :rtype: dict
    """
    return self._left_unary_operators_funcs


def get_right_unary_operators(self):
    """
    Get all right unary operators str symbol representation as set

    :return: all right unary operator symbols
    :rtype: dict
    """
    return self._right_unary_operators_funcs


def get_binary_operators(self):
    """
    Get all binary operators str symbol representation as set

    :return: all binary operator symbols
    :rtype: dict
    """
    return self._binary_operators_funcs


def get_precedence_for_operator(self, operator):
    """
    :param operator: a valid operator
    :type operator: str
    :return: precedence of operator
    :rtype: int | None #TODO review rtype..
    """
    if operator in self._left_unary_operators_funcs:
        return self._left_unary_operators_funcs.get(operator).get_precedence()
    if operator in self._right_unary_operators_funcs:
        return self._right_unary_operators_funcs.get(operator).get_precedence()
    elif operator in self._binary_operators_funcs:
        return self._binary_operators_funcs.get(operator).get_precedence()
    return None


def is_left_unary_operator(self, operator: str) -> bool:  # TODO: change func to check if in _left_unary_operators_funcs
    """
    Check if the given operator is a left unary operator.

    :param operator: a mathematical operator
    :type operator: str
    :return: True if operator is a left unary operator, otherwise False.
    :rtype: bool
    """
    return operator in self._left_unary_operators_funcs