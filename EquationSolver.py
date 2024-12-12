# File contains prints for dev tests
from OperatorsFactory import OperatorFactory

operator_factory = OperatorFactory()
unary_operators_dict = operator_factory.get_unary_operators()
binary_operators_dict = operator_factory.get_binary_operators()
operators_dict = {**unary_operators_dict, **binary_operators_dict} # Merges both dictionaries into a single dictionary

class EquationSolver:
    def __init__(self, equation: str):
        """
        Solves the equation.

        :param equation: User's input.
        :type equation: str
        """
        self.equation = equation
        self.tokens = []
        self.prefix_stack = []
        self.result = None

    def solve(self):
        """
        Solves the equation by calling the class' functions.

        :return: Solution to equation
        :rtype: float
        """
        self.tokenize()
        self.infix_to_postfix()
        self.solve_postfix()
        return self.result

    def tokenize(self): # TODO: check theres a maximum one . (dot) in operand.
        """
        Converts the str equation into a list of tokens.
        """
        tokens = []
        number = ''
        for character in self.equation:
            if character.isdigit() or character == '.':
                number += character
            else:
                if number != '':
                    tokens.append(number)
                    number = ''
                if character in operators_dict or character in '()':
                    tokens.append(character)
        if number != '':
            tokens.append(number)
        self.tokens = tokens
        # print(self.tokens) # For testing

    def precedence(self, operator):
        return operator_factory.get_precedence(operator)

    def infix_to_postfix(self):
        """
        Converts the tokenized infix equation to a postfix stack.
        """
        stack = []
        postfix = []

        for token in self.tokens:
            if token.isdigit() or '.' in token:  # Operand
                postfix.append(token)
            elif token == '(':
                stack.append(token)
            elif token == ')':
                while stack[-1] != '(':
                    postfix.append(stack.pop())
                stack.pop()
            else:  # Operator
                while stack and stack[-1] != '(' and self.precedence(token) <= self.precedence(stack[-1]):
                    postfix.append(stack.pop())
                stack.append(token)

        while stack:
            postfix.append(stack.pop())

        self.prefix_stack = postfix
        # print(f"Prefix stack: {self.prefix_stack}")  # For testing

    def solve_postfix(self):
        """
        Solves the equation represented by postfix stack and updates the result.
        """

        stack = []
        for token in (self.prefix_stack):
            if token.isdigit() or '.' in token:  # Operand
                stack.append(float(token))
            else:
                operand1 = stack.pop()
                # Temp implementation.
                # TODO: improve. avoid messy if-elif-else struct.
                if token in unary_operators_dict:
                    unary_result = unary_operators_dict.get(token).solve(operand1)
                    stack.append(unary_result)
                elif token in binary_operators_dict:
                    operand2 = stack.pop()
                    binary_result = binary_operators_dict.get(token).solve(operand2, operand1)
                    stack.append(binary_result)
        self.result = stack[0] if stack else None