# General idea, nothing serious for now

from abc import ABC, abstractmethod

class OperandBinary(ABC):
    """
    Abstract class for binary operand
    """
    @abstractmethod
    def solve(self, operand1, operand2):
        """
        Method to solve the mathematical expression.
        """
        pass