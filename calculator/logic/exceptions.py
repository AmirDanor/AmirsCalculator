from calculator.utils import operator_utils, general_utils


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
        forbidden_chars_from_string = {char for char in self._string if
                                       char not in general_utils.VALID_INPUT_CHARACTERS}
        return f'Error! Your input contains forbidden characters: {forbidden_chars_from_string}'


class NonIntFactorialError(Exception):
    def __init__(self, operand: float):
        """
        :param operand: Non-int operand which raised the exception
        :type operand: float
        """
        self._operand = operand

    def __str__(self):
        """
        :return: Message about the cause of the exception
        :rtype: str
        """
        return f"Error! Can't calculate factorial for non-integer operand: {self._operand}"


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
        return f"Error! Operand {self._operand} is too large for sum calculation"


class ZeroBaseNegExError(Exception):
    def __init__(self, exponent: float):
        """
        :param exponent: Negative exponent which raised the exception
        :type exponent: float
        """
        self._exponent = exponent

    def __str__(self):
        """
        :return: Message about the cause of the exception
        :rtype: str
        """
        return f"Error! Can't calculate negative exponent for zero base: 0{operator_utils.POWER}{self._exponent}"


class NegativeRootError(Exception):
    def __init__(self, base: float, exponent: float):
        """
        :param base: Base which raised the exception
        :type base: float
        :param exponent: Exponent which raised the exception
        :type exponent: float
        """
        self._base = base
        self._exponent = exponent

    def __str__(self):
        """
        :return: Message about the cause of the exception
        :rtype: str
        """
        return f"Error! Can't calculate negative root: {general_utils.OPEN_BRACKETS}{self._base}{general_utils.CLOSE_BRACKETS}{operator_utils.POWER}{self._exponent}"


class UnaryError(Exception):
    def __init__(self, sign: str):
        """
        :param sign: Sign representation of invalid unary operator
        :type sign: str
        """
        if sign == operator_utils.UNARY_MINUS:
            sign = operator_utils.MINUS
        self._sign = sign

    def __str__(self):
        """
        :return: Message about the cause of the exception
        :rtype: str
        """
        return f'Error! Wrong usage of unary operator: {self._sign}'


class UnmatchedOpeningParenthesesError(Exception):
    def __init__(self, index: int):
        self._index = index

    def __str__(self):
        """
        :return: Message about the cause of the exception
        :rtype: str
        """
        return f"Error! Unmatched opening parenthesis for '{general_utils.OPEN_BRACKETS}' at index {self._index}"


class UnmatchedClosingParenthesesError(Exception):
    def __init__(self, index: int):
        self._index = index

    def __str__(self):
        """
        :return: Message about the cause of the exception
        :rtype: str
        """
        return f"Error! Unmatched closing parenthesis for '{general_utils.CLOSE_BRACKETS}' at index {self._index}"


class EmptyParenthesesError(Exception):
    # todo: maybe define init
    def __str__(self):
        """
        :return: Message about the cause of the exception
        :rtype: str
        """
        return 'Error! Equation contains empty Parentheses'  # todo: maybe add index too?


class SingleDotError(Exception):
    def __str__(self):
        """
        :return: Message about the cause of the exception
        :rtype: str
        """
        return f'Error! Could not evaluate a single dot'


class MultipleDotsError(Exception):
    def __init__(self, dot_amount: int):
        """
        :param dot_amount: Amount of dots in a row, in invalid token
        :type dot_amount: int
        """
        self._dot_amount = dot_amount

    def __str__(self):
        """
        :return: Message about the cause of the exception
        :rtype: str
        """
        return f'Error! Could not evaluate {self._dot_amount} dots in a row'


class MultipleDotsOperandError(Exception):
    def __init__(self, token: str, dot_amount: int):
        """
        :param token: Invalid tokenized 'operand' which contains multiple points
        :type token: str
        :param dot_amount: Amount of dots in invalid token
        :type dot_amount: int
        """
        self._token = token
        self._dot_amount = dot_amount

    def __str__(self):
        """
        :return: Message about the cause of the exception
        :rtype: str
        """
        return f'Error! Could not refer to {self._token} as operand since it contains {self._dot_amount} dots'
