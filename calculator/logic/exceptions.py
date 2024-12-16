from calculator.utils import operator_utils


class InvalidInputError(Exception):
    def __init__(self, string):
        """
        :param string: User input which caused the exception
        :type string: str
        """
        self._string = string
    def __str__(self):
        """
        :return: Detailed message about the forbidden chars used in users input
        :rtype: str
        """
        forbidden_chars_from_string = {char for char in self._string if char not in operator_utils.VALID_INPUT_CHARACTERS}
        return f'Error! Your input contains forbidden characters: {forbidden_chars_from_string}'

class NegativeFactorialError(Exception):
    def __init__(self, operand: float):
        """
        :param operand: Negative operand which raised the exception
        :type operand: float
        """
        self._operand = operand
    def __str__(self):
        """
        :return: Message about the cause of the exception
        :rtype: str
        """
        return f"Error! Can't calculate factorial for negative operand: {self._operand}"

class LargeFactorialError(Exception):
    def __init__(self, operand: float):
        """
        :param operand: Large operand which raised the exception
        :type operand: float
        """
        self._operand = operand
    def __str__(self):
        """
        :return: Message about the cause of the exception
        :rtype: str
        """
        return f"Error! Operand {self._operand} is too large for factorial calculation"

class NegativeSumError(Exception):
    def __init__(self, operand: float):
        """
        :param operand: Negative operand which raised the exception
        :type operand: float
        """
        self._operand = operand
    def __str__(self):
        """
        :return: Message about the cause of the exception
        :rtype: str
        """
        return f"Error! Can't calculate sum for negative operand: {self._operand}"

class LargeSumError(Exception):
    def __init__(self, number: float):
        """
        :param number: Large number which raised the exception
        :type number: float
        """
        self._number = number
    def __str__(self):
        """
        :return: Message about the cause of the exception
        :rtype: str
        """
        return f"Error! Number {self._number} is too large for sum calculation"

class UnaryError(Exception):
    def __init__(self, sign: str):
        """
        :param sign: Sign representation of invalid unary operator
        :type sign: str
        """
        if sign == operator_utils.SIGN_UNARY_MINUS:
            sign = '-'
        self._sign = sign
    def __str__(self):
        """
        :return: Message about the cause of the exception
        :rtype: str
        """
        return f'Error! Wrong usage of unary operator: {self._sign}' #todo: maybe add index too?

class EmptyParenthesesError(Exception):
       # todo: maybe define init
    def __str__(self):
        """
        :return: Message about the cause of the exception
        :rtype: str
        """
        return 'Error! Equation contains empty Parentheses' #todo: maybe add index too?