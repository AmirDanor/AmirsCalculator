"""
Module contains classes abstract classes and actual classes for all
relevant operators.
Each operator has precedence, and a solve method.
Unary operators only got is_left method which returns bool True if
the operand is left-sided, False otherwise
"""

import math
from abc import ABC, abstractmethod

from calculator.logic.exceptions import NegativeFactorialError, \
    NegativeSumError, LargeSumError, LargeFactorialError, \
    NonIntFactorialError, NegativeRootError, ZeroBaseNegExError, \
    DivisionByZeroError, ModuloByZeroError
from calculator.utils import general_utils, operator_utils


class Operator(ABC):
    """
    Abstract class for operator
    """

    @abstractmethod
    def get_precedence(self) -> int:
        """
        Method returns operator's precedence.
        """

        pass


class UnaryOperator(Operator):
    """
    Abstract class for unary operand
    """

    @abstractmethod
    def solve(self, operand: float):
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
    def solve(self, operand1: float, operand2: float) -> float:
        """
        Method to solve the mathematical binary expression.
        """

        pass


class Add(BinaryOperator):
    def get_precedence(self) -> int:
        """
        :return: Operator's precedence.
        :rtype: int
        """

        return 1

    def solve(self, operand1: float, operand2: float) -> float:
        # self-explanatory
        return operand1 + operand2


class Sub(BinaryOperator):
    def get_precedence(self) -> int:
        """
        :return: Operator's precedence.
        :rtype: int
        """

        return 1

    def solve(self, operand1: float, operand2: float) -> float:
        # self-explanatory
        return operand1 - operand2


class Mul(BinaryOperator):
    def get_precedence(self) -> int:
        """
        :return: Operator's precedence.
        :rtype: int
        """

        return 2

    def solve(self, operand1: float, operand2: float) -> float:
        # self-explanatory
        return operand1 * operand2


class Div(BinaryOperator):
    def get_precedence(self) -> int:
        """
        :return: Operator's precedence.
        :rtype: int
        """

        return 2

    def solve(self, operand1: float, operand2: float) -> float:
        """
        Solves division between operand1 and operand2.

        :param operand1: Dividend.
        :type operand1: float
        :param operand2: Divisor.
        :type operand2: float
        :raises DivisionByZeroError: If operand2 is zero.
        :return: Result of dividend divided by divisor (quotient).
        :rtype: float
        """

        try:
            return operand1 / operand2
        except ZeroDivisionError:
            raise DivisionByZeroError(operand1)


class Pow(BinaryOperator):
    def get_precedence(self) -> int:
        """
        :return: Operator's precedence.
        :rtype: int
        """

        return 4

    def solve(self, base: float, exponent: float) -> float:
        """
        Solves base to the power of exponent.

        :param base: Power operation's base.
        :type base: float
        :param exponent: Power operation's exponent.
        :type exponent: float
        :raises ZeroBaseNegExError: If base is zero and
            exponent is negative.
        :raises NegativeRootError: If base is negative and exponent
            is fraction.
        :return: Result of base to the power of exponent.
        :rtype: float
        """

        if base == 0 and exponent < 0:
            raise ZeroBaseNegExError(exponent)
        elif base < 0 and not exponent.is_integer():
            raise NegativeRootError(base, exponent)
        return math.pow(base, exponent)


class Mod(BinaryOperator):
    def get_precedence(self) -> int:
        """
        :return: Operator's precedence.
        :rtype: int
        """

        return 5

    def solve(self, operand1: float, operand2: float) -> float:
        """
        Solves modulo between operand1 and operand2.

        :param operand1: Operand1.
        :type operand1: float
        :param operand2: Operand2.
        :type operand2: float
        :raises ModuloByZeroError: If operand2 is zero.
        :return: Result of Operand1 modulo Operand2.
        :rtype: float
        """

        try:
            return operand1 % operand2
        except ZeroDivisionError:
            raise ModuloByZeroError(operand1)


class Max(BinaryOperator):
    def get_precedence(self) -> int:
        """
        :return: Operator's precedence.
        :rtype: int
        """

        return 6

    def solve(self, operand1: float, operand2: float) -> float:
        # self-explanatory
        return max(operand1, operand2)


class Min(BinaryOperator):
    def get_precedence(self) -> int:
        """
        :return: Operator's precedence.
        :rtype: int
        """

        return 6

    def solve(self, operand1: float, operand2: float) -> float:
        # self-explanatory
        return min(operand1, operand2)


class Avg(BinaryOperator):
    def get_precedence(self) -> int:
        """
        :return: Operator's precedence.
        :rtype: int
        """

        return 6

    def solve(self, operand1, operand2):  # self-explanatory
        return (operand1 + operand2) / 2


class UMin(UnaryOperator):
    def get_precedence(self) -> int:
        """
        :return: Operator's precedence.
        :rtype: int
        """

        return 3

    def is_left(self) -> bool:
        """
        :return: if unary operator is a left operator
        :rtype: bool
        """

        return True

    def solve(self, operand: float) -> float:
        """
        Returns operand after using unary minus on it.

        :param operand: Operand.
        :type operand: float
        :return: Operand after unary minus operation.
        :rtype: float
        """

        return -operand


class Neg(UnaryOperator):
    def get_precedence(self) -> int:
        """
        :return: Operator's precedence.
        :rtype: int
        """

        return 7

    def is_left(self) -> bool:
        """
        :return: If unary operator is a left operator.
        :rtype: bool
        """

        return True

    def solve(self, operand: float) -> float:
        """
        Returns negative value of operand.

        :param operand: operand.
        :type operand: float
        :return: negative value of operand.
        :rtype: float
        """

        return -operand


class Fac(UnaryOperator):
    def get_precedence(self) -> int:
        """
        :return: Operator's precedence.
        :rtype: int
        """

        return 7

    def is_left(self) -> bool:
        """
        :return: If unary operator is a left operator.
        :rtype: bool
        """

        return False

    def solve(self, operand: float) -> float:
        """
        Solves factorial for operand

        :param operand: Operand.
        :type operand: float
        :raises NegativeFactorialError: If factorial's operand is negative.
        :raises LargeFactorialError: If factorial's operand is larger
            than allowed.
        :raises NonIntFactorialError: If factorial's operand is not
            an integer.
        :return: Result of factorial operation on operand.
        :rtype: float
        """

        if operand < 0:
            raise NegativeFactorialError(operand)
        elif operand > operator_utils.FACTORIAL_MAX_OPERAND:
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
        :return: Operator's precedence.
        :rtype: int
        """

        return 7

    def is_left(self) -> bool:
        """
        :return: If unary operator is a left operator.
        :rtype: bool
        """

        return False

    def solve(self, operand: float) -> float:
        """
        Calculate and return the sum of all digit-numbers in number.

        :param operand: operand.
        :type operand: float
        :return: operand after sum operation.
        :rtype: float
        :raises NegativeSumError: if operand is negative.
        :raises LargeSumError: if operand is too large.
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
