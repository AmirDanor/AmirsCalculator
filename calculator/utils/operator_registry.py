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

    def get_unary_operators(self) -> dict:
        """
        Get unary operators dict which maps str symbol to class.

        :return: Unary operators dict which maps str symbol to class.
        :rtype: dict
        """

        merged_unary_dict = {**self._left_unary_operators_funcs,
                             **self._right_unary_operators_funcs}
        return merged_unary_dict

    def get_left_unary_operators(self) -> dict:
        """
        Get left unary operators dict which maps str symbol to class.

        :return: Left unary operators dict which maps str symbol to class.
        :rtype: dict
        """

        return self._left_unary_operators_funcs

    def get_right_unary_operators(self) -> dict:
        """
        Get right unary operators dict which maps str symbol to class.

        :return: Right unary operators dict which maps str symbol to class.
        :rtype: dict
        """

        return self._right_unary_operators_funcs

    def get_binary_operators(self) -> dict:
        """
        Get binary operators dict which maps str symbol to class.

        :return: Binary operators dict which maps str symbol to class.
        :rtype: dict
        """

        return self._binary_operators_funcs

    def get_all_operators(self) -> dict:
        """
        Get all operators dict which maps str symbol to class.

        :return: All operators dict which maps str symbol to class.
        :rtype: dict
        """

        all_operators_dict = {**self._left_unary_operators_funcs,
                              **self._right_unary_operators_funcs,
                              **self._binary_operators_funcs}
        return all_operators_dict

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
