"""
Module which maintains a dictionary which maps each operand symbol
to its class.
contains methods to ease the usage of the classes.
"""
from calculator.utils.operators import Add, Sub, Mul, Div, UMin, Pow, Mod, \
    Max, Min, Avg, Neg, Fac, Sum


class OperatorRegistry:
    """
    A registry for mapping operator functions by string representation
    (Using Dictionaries). Separate dictionaries for unary / binary operators.
    """

    def __init__(self):
        """
        Initialize the operator dictionaries (separated by unary /
        binary) with default binary and unary operators.
        """

        self._left_unary_operators_funcs = {
            ';': UMin(),
            '~': Neg()
        }
        self._right_unary_operators_funcs = {
            '!': Fac(),
            '#': Sum()
        }
        self._binary_operators_funcs = {
            '+': Add(),
            '-': Sub(),
            '*': Mul(),
            '/': Div(),
            '^': Pow(),
            '%': Mod(),
            '$': Max(),
            '&': Min(),
            '@': Avg()
        }

    def get_unary_operators(self):
        """
        Get all unary operators str symbol representation as set.

        :return: all unary operator symbols.
        :rtype: dict
        """

        merged_unaries_dict = {**self._left_unary_operators_funcs,
                               **self._right_unary_operators_funcs}
        return merged_unaries_dict

    def get_left_unary_operators(self):
        """
        Get all left unary operators str symbol representation as set.

        :return: all left unary operator symbols.
        :rtype: dict
        """

        return self._left_unary_operators_funcs

    def get_right_unary_operators(self):
        """
        Get all right unary operators str symbol representation as set.

        :return: all right unary operator symbols.
        :rtype: dict
        """

        return self._right_unary_operators_funcs

    def get_binary_operators(self):
        """
        Get all binary operators str symbol representation as set.

        :return: all binary operator symbols.
        :rtype: dict
        """

        return self._binary_operators_funcs

    def get_precedence(self, operator):
        """
        :param operator: a valid operator.
        :type operator: str
        :return: precedence of operator.
        :rtype: int or None
        """

        if operator in self._left_unary_operators_funcs:
            return self._left_unary_operators_funcs.get(
                operator).get_precedence()
        if operator in self._right_unary_operators_funcs:
            return self._right_unary_operators_funcs.get(
                operator).get_precedence()
        elif operator in self._binary_operators_funcs:
            return self._binary_operators_funcs.get(operator).get_precedence()
        return None

