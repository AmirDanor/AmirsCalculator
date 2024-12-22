"""
Operand utils module which contains operand-related constants used across the
calculator.
"""

# Methods
from calculator.utils import general_utils, operator_utils


def is_operand(string: str) -> bool:
    """
    Checks if string is operand.

    :param string: string to check.
    :type string: str
    :return: True if string is operand, else return False.
    :rtype: bool
    """

    return (string.isdigit() or general_utils.DOT in string
            or operator_utils.SIGN_MINUS_SYMBOL in string)
