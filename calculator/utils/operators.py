import math
from abc import ABC, abstractmethod

from calculator.logic.exceptions import NegativeFactorialError, \
    NegativeSumError, LargeSumError, LargeFactorialError, \
    NonIntFactorialError, NegativeRootError, ZeroBaseNegExError, \
    DivisionByZeroError, ModuloByZeroError
from calculator.utils import general_utils


class Operator(ABC):
    """
    Abstract class for operator
    """

    @abstractmethod
    def get_precedence(self):
        """
        Method returns operator's precedence.
        """

        pass


class UnaryOperator(Operator):
    """
    Abstract class for unary operand
    """

    @abstractmethod
    def solve(self, operand):
        """
        Method to solve the mathematical unary expression.
        """

        pass

    @abstractmethod
    def is_left(self) -> bool:
        """
        :return: if unary operator should be placed to the left of the
            operand (True) / to the right (False)
        :rtype: bool
        """

        pass


class BinaryOperator(Operator):
    """
    Abstract class for binary operand
    """

    @abstractmethod
    def solve(self, operand1, operand2):
        """
        Method to solve the mathematical binary expression.
        """

        pass


class Add(BinaryOperator):
    def get_precedence(self):
        return 1

    def solve(self, operand1, operand2):  # self-explanatory
        return operand1 + operand2


class Sub(BinaryOperator):
    def get_precedence(self) -> int:
        """
        :return: operator's precedence
        :rtype: int
        """

        return 1

    def solve(self, operand1, operand2):  # self-explanatory
        return operand1 - operand2


class Mul(BinaryOperator):
    def get_precedence(self) -> int:
        """
        :return: operator's precedence
        :rtype: int
        """

        return 2

    def solve(self, operand1, operand2):  # self-explanatory
        return operand1 * operand2


class Div(BinaryOperator):
    def get_precedence(self) -> int:
        """
        :return: operator's precedence
        :rtype: int
        """

        return 2

    def solve(self, operand1, operand2):
        """
        Solves division between operand1 and operand2.

        :param operand1: Dividend
        :type operand1: float
        :param operand2: Divisor
        :type operand2: float
        :raises DivisionByZeroError: If operand2 is zero.
        """

        try:
            return operand1 / operand2
        except ZeroDivisionError:
            raise DivisionByZeroError(operand1)


class Pow(BinaryOperator):
    def get_precedence(self) -> int:
        """
        :return: operator's precedence
        :rtype: int
        """

        return 4

    def solve(self, base, exponent):
        if base == 0 and exponent < 0:
            raise ZeroBaseNegExError(exponent)
        elif base < 0 and not exponent.is_integer():
            raise NegativeRootError(base, exponent)
        return math.pow(base, exponent)


class Mod(BinaryOperator):
    def get_precedence(self) -> int:
        """
        :return: operator's precedence
        :rtype: int
        """

        return 5

    def solve(self, operand1, operand2):
        try:
            return operand1 % operand2
        except ZeroDivisionError:
            raise ModuloByZeroError(operand1)


class Max(BinaryOperator):
    def get_precedence(self) -> int:
        """
        :return: operator's precedence
        :rtype: int
        """

        return 6

    def solve(self, operand1, operand2):
        return max(operand1, operand2)


class Min(BinaryOperator):
    def get_precedence(self) -> int:
        """
        :return: operator's precedence
        :rtype: int
        """

        return 6

    def solve(self, operand1, operand2):
        return min(operand1, operand2)


class Avg(BinaryOperator):
    def get_precedence(self) -> int:
        """
        :return: operator's precedence
        :rtype: int
        """

        return 6

    def solve(self, operand1, operand2):
        return (operand1 + operand2) / 2


class UMin(UnaryOperator):
    def get_precedence(self) -> int:
        """
        :return: operator's precedence
        :rtype: int
        """

        return 3

    def is_left(self):
        """
        :return: if unary operator is a left operator
        :rtype: bool
        """

        return True

    def solve(self, operand):
        """
        Returns operand after using unary minus on it.

        :param operand: Operand
        :type operand: float
        :return: Operand after unary minus operation
        :rtype: float
        """

        return -operand


class Neg(UnaryOperator):
    def get_precedence(self) -> int:
        """
        :return: operator's precedence
        :rtype: int
        """

        return 7

    def is_left(self):
        """
        :return: if unary operator is a left operator
        :rtype: bool
        """

        return True

    def solve(self, operand):
        """
        Returns negative value of operand.

        :param operand: operand
        :type operand: float
        :return: negative value of operand
        :rtype: float
        """

        return -operand


class Fac(UnaryOperator):
    def get_precedence(self) -> int:
        """
        :return: operator's precedence
        :rtype: int
        """

        return 7

    def is_left(self):
        """
        :return: if unary operator is a left operator
        :rtype: bool
        """

        return False

    def solve(self, operand):
        if operand < 0:
            raise NegativeFactorialError(operand)
        elif operand > general_utils.FACTORIAL_MAX_OPERAND:
            raise LargeFactorialError(operand)
        elif not operand.is_integer():
            raise NonIntFactorialError(operand)
        result = 1
        for index in range(1, int(operand) + 1):
            result = result * index
        return result


class Sum(UnaryOperator):
    def get_precedence(self) -> int:
        """
        :return: operator's precedence
        :rtype: int
        """

        return 7

    def is_left(self):
        """
        :return: if unary operator is a left operator
        :rtype: bool
        """

        return False

    def solve(self, operand):
        """
        Calculate and return the sum of all digit-numbers in number.

        :param operand: operand
        :type operand: float
        :return: operand after sum operation
        :rtype: float
        :raises NegativeSumError: if operand is negative
        :raises LargeSumError: if operand is too large
        """

        if operand < 0:
            raise NegativeSumError(operand)
        if 'e' in str(operand):
            raise LargeSumError(operand)
        operand_as_str = str(operand).replace(general_utils.DOT,
                                              general_utils.EMPTY_STR)
        result = 0.0

        for char in operand_as_str:
            result += float(char)
        return result
