"""
Module consists of custom exceptions.
Used to validate proper calculator functionality.
"""

from calculator.utils import operator_utils, general_utils


class EmptyEquationError(Exception):
    """
    Exception for empty equation.
    """

    def __str__(self):
        return "Nothing To Calculate!"


class InvalidInputError(Exception):
    """
    Exception for displaying all invalid chars entered by user.
    """

    def __init__(self, string: str):
        """
        :param string: User input which caused the exception.
        :type string: str
        """

        self._string = string

    def __str__(self):
        """
        :return: Detailed message about the forbidden chars used in users
            input.
        :rtype: str
        """
        forbidden_chars_from_string = {char for char in self._string
                                       if char not in
                                       general_utils.VALID_INPUT_CHARACTERS}
        return (f'Error! Your input contains forbidden'
                f' characters: {forbidden_chars_from_string}')


class EndMinusesError(Exception):
    """
    Exception for equations which end with minuses.
    """

    def __init__(self, amount: int):
        """
        :param amount: Amount of minuses at the end of equation.
        :type amount: int
        """

        self._amount = amount

    def __str__(self):
        """
        :return: Message about the cause of the exception.
        :rtype: str
        """
        return (f'Error! Equation ends with {self._amount} minuses with no '
                f'operand after')


class DivisionByZeroError(Exception):
    """
    Exception for trying to perform division operation with zero as divisor.
    """

    def __init__(self, operand: float):
        """
        :param operand: Operand which was attempted to be divided by 0.
        :type operand: float
        """

        self._operand = operand

    def __str__(self):
        """
        :return: Message about the cause of the exception.
        :rtype: str
        """

        return (f"Error! Can't divide operand"
                f" {self._operand} by zero")


class ModuloByZeroError(Exception):
    """
    Exception for trying to perform modulo operation with zero as divisor.
    """

    def __init__(self, operand: float):
        """
        :param operand: Operand which was attempted to be divided by 0 in
            modulo operation.
        :type operand: float
        """
        self._operand = operand

    def __str__(self):
        """
        :return: Message about the cause of the exception.
        :rtype: str
        """

        return (f"Error! Can't divide operand"
                f" {self._operand} by zero in modulo operation")


class NonIntFactorialError(Exception):
    """
    Exception for trying to calculate factorial of a non-int operand.
    """

    def __init__(self, operand: float):
        """
        :param operand: Non-int operand which raised the exception.
        :type operand: float
        """

        self._operand = operand

    def __str__(self):
        """
        :return: Message about the cause of the exception.
        :rtype: str
        """

        return (f"Error! Can't calculate factorial for"
                f" non-integer operand: {self._operand}")


class NegativeFactorialError(Exception):
    """
    Exception for trying to calculate factorial of a negative operand.
    """

    def __init__(self, operand: float):
        """
        :param operand: Negative operand which raised the exception.
        :type operand: float
        """

        self._operand = operand

    def __str__(self):
        """
        :return: Message about the cause of the exception.
        :rtype: str
        """

        return (f"Error! Can't calculate factorial for"
                f" negative operand: {self._operand}")


class LargeFactorialError(Exception):
    """
    Exception for trying to calculate factorial on a large operand.
    """

    def __init__(self, operand: float):
        """
        :param operand: Large operand which raised the exception.
        :type operand: float
        """

        self._operand = operand

    def __str__(self):
        """
        :return: Message about the cause of the exception.
        :rtype: str
        """

        return (f"Error! Operand {self._operand} is too"
                f" large for factorial calculation")


class NegativeSumError(Exception):
    """
    Exception for trying to sum a negative operand.
    """

    def __init__(self, operand: float):
        """
        :param operand: Negative operand which raised the exception.
        :type operand: float
        """

        self._operand = operand

    def __str__(self):
        """
        :return: Message about the cause of the exception.
        :rtype: str
        """

        return (f"Error! Can't calculate sum for"
                f" negative operand: {self._operand}")


class LargeSumError(Exception):
    """
    Exception for trying to sum a large operand.
    """

    def __init__(self, operand: float):
        """
        :param operand: Large operand which raised the exception.
        :type operand: float
        """

        self._operand = operand

    def __str__(self):
        """
        :return: Message about the cause of the exception.
        :rtype: str
        """

        return (f"Error! Operand {self._operand}"
                f" is too large for sum calculation")


class ZeroBaseNegExError(Exception):
    """
    Exception for trying to raise zero to the power of a negative exponent.
    """

    def __init__(self, exponent: float):
        """
        :param exponent: Negative exponent which raised the exception.
        :type exponent: float
        """

        self._exponent = exponent

    def __str__(self):
        """
        :return: Message about the cause of the exception.
        :rtype: str
        """

        return (f"Error! Can't calculate negative exponent for zero base:"
                f" 0{operator_utils.POW_SYMBOL}{self._exponent}")


class NegativeRootError(Exception):
    """
    Exception for trying to calculate a negative root.
    """

    def __init__(self, base: float, exponent: float):
        """
        :param base: Base which raised the exception.
        :type base: float
        :param exponent: Exponent which raised the exception.
        :type exponent: float
        """

        self._base = base
        self._exponent = exponent

    def __str__(self):
        """
        :return: Message about the cause of the exception.
        :rtype: str
        """

        return (
            f"Error! Can't calculate negative root: "
            f"{general_utils.OPEN_BRACKETS}{self._base}"
            f"{general_utils.CLOSE_BRACKETS}"
            f"{operator_utils.POW_SYMBOL}{self._exponent}"
        )


class OperatorUsageError(Exception):
    """
    Exception for misusing an operator.
    """

    def __init__(self, sign: str, desc: str):
        """
        :param sign: Sign representation of operator which was used
            incorrectly.
        :type sign: str
        :param desc: Short description which specifies the wrong usage.
        :type desc: str
        """

        self._sign = sign
        self._desc = desc

    def __str__(self):
        """
        :return: Message about the cause of the exception.
        :rtype: str
        """

        return f'Error! Wrong usage of operator: {self._sign}, {self._desc}'


class UnaryError(Exception):
    """
    Exception for misusing a unary operator.
    """

    def __init__(self, sign: str, is_left_error: bool):
        """
        :param sign: Sign representation of invalid unary operator.
        :type sign: str
        """

        if sign == operator_utils.UNARY_MINUS_SYMBOL:
            sign = operator_utils.SUB_SYMBOL
        self._sign = sign
        self._unary_side = 'right'
        is_left_unary = sign in operator_utils.LEFT_UNARY_OPERATORS
        if is_left_unary:
            self._unary_side = 'left'
        self._error_side = 'right'
        if is_left_error:
            self._error_side = 'left'

    def __str__(self):
        """
        :return: Message about the cause of the exception.
        :rtype: str
        """

        return (f'Error! Wrong parameter to the {self._error_side} of the '
                f'{self._unary_side} unary operator: {self._sign}')


class WrongParenthesesUsageError(Exception):
    """
    Exception for misusing parentheses.
    """

    def __str__(self):
        """
        :return: Message about the cause of the exception - Wrong
            parentheses usage in equation.
        :rtype: str
        """

        return (f"Error! Equation contains wrong parentheses usage."
                f" make sure parentheses are treated like operands!")


class UnmatchedOpeningParenthesesError(Exception):
    """
    Exception for an opening parentheses with no matching closing one.
    """

    def __init__(self, index: int):
        """
        :param index: Index of an opening parentheses with no matching
            closing parentheses in user's input.
        :type index: int
        """

        self._index = index

    def __str__(self):
        """
        :return: Message about the cause of the exception.
        :rtype: str
        """

        return (f"Error! Unmatched opening parenthesis for"
                f" '{general_utils.OPEN_BRACKETS}' at index {self._index}")


class UnmatchedClosingParenthesesError(Exception):
    """
    Exception for a closing parentheses with no matching opening one.
    """

    def __init__(self, index: int):
        """
        :param index: Index of a closing parentheses with no matching
            opening parentheses in user's input.
        :type index: int
        """

        self._index = index

    def __str__(self):
        """
        :return: Message about the cause of the exception.
        :rtype: str
        """

        return (f"Error! Unmatched closing parenthesis for"
                f" '{general_utils.CLOSE_BRACKETS}' at index {self._index}")


class EmptyParenthesesError(Exception):
    """
    Exception for empty parentheses in equation.
    """

    def __init__(self, opening_index: int, closing_index: int):
        """
        :param opening_index: Index of opening parentheses.
        :type opening_index: int
        :param closing_index: Index of closing parentheses.
        :type closing_index: int
        """

        self._closing_index = closing_index
        self._opening_index = opening_index

    def __str__(self):
        """
        :return: Message about the cause of the exception.
        :rtype: str
        """

        return (f'Error! Equation contains empty Parentheses at indexes: '
                f'{self._opening_index}, {self._closing_index}')


class SingleDotError(Exception):
    """
    Exception for a single dot which can not be evaluated as part of an
        operand.
    """

    def __str__(self):
        """
        :return: Message about the cause of the exception.
        :rtype: str
        """

        return f'Error! Could not evaluate a single dot'


class MultipleDotsError(Exception):
    """
    Exception for multiple dots which can not be evaluated.
    """

    def __init__(self, dot_amount: int):
        """
        :param dot_amount: Amount of dots in a row, in invalid token.
        :type dot_amount: int
        """

        self._dot_amount = dot_amount

    def __str__(self):
        """
        :return: Message about the cause of the exception.
        :rtype: str
        """

        return f'Error! Could not evaluate {self._dot_amount} dots in a row'


class MultipleDotsOperandError(Exception):
    """
    Exception for 'operand' which contains multiple dots.
    """

    def __init__(self, token: str, dot_amount: int):
        """
        :param token: Invalid tokenized 'operand' which contains multiple
            points.
        :type token: str
        :param dot_amount: Amount of dots in invalid
            token.
        :type dot_amount: int
        """

        self._token = token
        self._dot_amount = dot_amount

    def __str__(self):
        """
        :return: Message about the cause of the exception.
        :rtype: str
        """

        return (f'Error! Could not refer to {self._token} as operand since it '
                f'contains {self._dot_amount} dots')


class ExpectedOperandError(Exception):
    """
    Exception for non-operand usage in equation where operand is expected.
    """

    def __init__(self, token: str):
        """
        :param token: Invalid token which appears instead of expected
            operand.
        :type token: str
        """

        self._token = token

    def __str__(self):
        """
        :return: Message about the cause of the exception.
        :rtype: str
        """
        if self._token == '--':
            return f'Error! Expected an operator after {self._token}'
        return f'Error! Expected an operator instead of {self._token}'
