from abc import ABC, abstractmethod

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

class Pow(BinaryOperator): # TODO: Make sure result is not too large. Throw a relevant exception if needed. [make sure for all operators...]
    def get_precedence(self):
        return 3
    def solve(self, operand1, operand2):
        return operand1 ** operand2

class Mod(BinaryOperator):
    def get_precedence(self):
        return 4
    def solve(self, operand1, operand2):
        return operand1 % operand2

class Max(BinaryOperator):
    def get_precedence(self):
        return 5
    def solve(self, operand1, operand2):
        return max(operand1, operand2)

class Min(BinaryOperator):
    def get_precedence(self):
        return 5
    def solve(self, operand1, operand2):
        return min(operand1, operand2)

class Avg(BinaryOperator):
    def get_precedence(self):
        return 5
    def solve(self, operand1, operand2):
        return (operand1 + operand2) / 2

class Neg(UnaryOperator):
    def get_precedence(self):
        return 6
    def solve(self, operand):
        return -operand

class Fac(UnaryOperator):
    def get_precedence(self):
        return 6
    def solve(self, operand): # TODO: Make sure operand is not negative. Throw a relevant exception if needed.
        operand = int(operand)
        result = 1
        for i in range(1, operand + 1):
            result = result * i
        return result

class Sum(UnaryOperator):
    def get_precedence(self):
        return 6
    def solve(self, operand): # TODO: check theres a maximum one . (dot) in operand before removal. Optimally check in tokenizer [EquationSolver.py] (in final version)!
        operand_as_str = str(operand).replace('.', '') # TODO: change/delete this line after optimizing tokenizer [EquationSolver.py]
        result = 0.0

        for char in operand_as_str:
            result += float(char)
        return result