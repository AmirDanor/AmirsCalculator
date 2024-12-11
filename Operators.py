# General idea, nothing serious for now

from abc import ABC, abstractmethod

class Operator(ABC):
    """
    Abstract class for operator
    """

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