from abc import ABC, abstractmethod
import math

from calculator.logic.exceptions import NegativeFactorialError, NegativeSumError, LargeSumError, LargeFactorialError, \
    NonIntFactorialError, NegativeRootError, ZeroBaseNegExError
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
        :return: if unary operator should be placed to the left of the operand (True) / to the right (False)
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
    def solve(self, operand1, operand2):
        return operand1 + operand2

class Sub(BinaryOperator):
    def get_precedence(self):
        return 1
    def solve(self, operand1, operand2):
        return operand1 - operand2

class Mul(BinaryOperator):
    def get_precedence(self):
        return 2
    def solve(self, operand1, operand2):
        return operand1 * operand2

class Div(BinaryOperator): # TODO: Make sure operand2 is not negative. Throw a relevant exception if needed.
    def get_precedence(self):
        return 2
    def solve(self, operand1, operand2):
        return operand1 / operand2

class Pow(BinaryOperator): # TODO: Make sure _result is not too large. Throw a relevant exception if needed. [make sure for all operators...]
    def get_precedence(self):
        return 4
    def solve(self, base, exponent):
        if base == 0 and exponent < 0:
            raise ZeroBaseNegExError(exponent)
        elif base < 0 and not exponent.is_integer():
            raise NegativeRootError(base, exponent)
        return math.pow(base, exponent)

class Mod(BinaryOperator):
    def get_precedence(self):
        return 5
    def solve(self, operand1, operand2):
        return operand1 % operand2

class Max(BinaryOperator):
    def get_precedence(self):
        return 6
    def solve(self, operand1, operand2):
        return max(operand1, operand2)

class Min(BinaryOperator):
    def get_precedence(self):
        return 6
    def solve(self, operand1, operand2):
        return min(operand1, operand2)

class Avg(BinaryOperator):
    def get_precedence(self):
        return 6
    def solve(self, operand1, operand2):
        return (operand1 + operand2) / 2

class UMin(UnaryOperator):
    def get_precedence(self):
        return 3
    def is_left(self):
        return True
    def solve(self, operand):
        return -operand

class Neg(UnaryOperator):
    def get_precedence(self):
        return 7
    def is_left(self):
        return True
    def solve(self, operand):
        return -operand

class Fac(UnaryOperator):
    def get_precedence(self):
        return 7
    def is_left(self):
        return False
    def solve(self, operand): # TODO: Make sure operand is a positive int. Throw a relevant exception if needed (different one for each case).
        if operand < 0:
            raise NegativeFactorialError(operand)
        elif operand > general_utils.FACTORICAL_MAX_OPERAND:
            raise LargeFactorialError(operand)
        elif not operand.is_integer():
            raise NonIntFactorialError(operand)
        result = 1
        for index in range(1, int(operand) + 1):
            result = result * index
        return result

class Sum(UnaryOperator):
    def get_precedence(self):
        return 7
    def is_left(self):
        return False
    def solve(self, operand): # TODO: check theres a maximum one . (dot) in operand before removal. Optimally check in tokenizer [equation_solver.py] (in final version)!
        if operand < 0:
            raise NegativeSumError(operand)
        if operand > 9999999999999999:
            raise LargeSumError(operand)
        operand_as_str = str(operand).replace('.', '') # TODO: change/delete this line after optimizing tokenizer [equation_solver.py]
        result = 0.0

        for char in operand_as_str:
            result += float(char)
        return result