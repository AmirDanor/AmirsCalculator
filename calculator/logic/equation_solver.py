# File contains prints for dev tests

from calculator.logic.operator_registry import OperatorRegistry
from calculator.logic.operators import UnaryOperator
from calculator.utils.operand_utils import SIGN_NUMBER_MINUS, is_operand, precedence

OPERATOR_REGISTRY = OperatorRegistry()
UNARY_OPERATORS_DICT = OPERATOR_REGISTRY.get_unary_operators()
BINARY_OPERATORS_DICT = OPERATOR_REGISTRY.get_binary_operators()
operators_dict = {**UNARY_OPERATORS_DICT, **BINARY_OPERATORS_DICT} # Merges both dictionaries into a single dictionary


class EquationSolver:
    def __init__(self, equation: list):
        """
        Solves the equation.

        :param equation: User's input.
        :type equation: list
        """
        self._tokens = equation
        self._postfix_stack = []
        self._result = None

    def solve(self):
        """
        Solves the equation by calling the class' functions.

        :return: Solution to equation
        :rtype: float
        """
        #self.tokenize()
        #self.delete_extra_minuses()
        #self.join_number_minuses()
        #self.replace_unary_minuses()
        self.infix_to_postfix()
        self.solve_postfix()
        #if self._result == -0.0:
        #    self._result = 0.0
        return self._result

    def infix_to_postfix(self):
        """
        Converts the tokenized infix equation to a postfix stack.
        """
        stack = []
        postfix = []
        index = 0
        for token in self._tokens:
            if is_operand(token) or SIGN_NUMBER_MINUS in token:  # Operand
                postfix.append(token)
            elif token is UnaryOperator:
                if OPERATOR_REGISTRY.is_left_unary_operator(token):  # Push left-sided unary operator
                    stack.append(token)
                else:  # Right-sided unary operators
                    if index > 0 and is_operand(self._tokens[index - 1]):
                        postfix.append(token)
                    else:
                        stack.append(token)
            elif token == '(':
                stack.append(token)
            elif token == ')':
                while stack[-1] != '(' and stack[-1] != SIGN_NUMBER_MINUS+'(':
                    postfix.append(stack.pop())
                if (stack[-1] != SIGN_NUMBER_MINUS+'('):
                    pass # Insert negative value of _result in brackets...
                stack.pop()
            else:  # Operator
                while stack and stack[-1] != '(' and precedence(token) <= precedence(stack[-1]): # add '-('
                    postfix.append(stack.pop())
                stack.append(token)
            index+=1

        while stack:
            postfix.append(stack.pop())

        self._postfix_stack = postfix
        # print(f"Postfix stack: {self._postfix_stack}")  # For testing

    def solve_postfix(self):
        """
        Solves the equation represented by postfix stack and updates the _result.
        """
        stack = []
        for token in (self._postfix_stack):
            if is_operand(token) or SIGN_NUMBER_MINUS in token:  # Operand
                stack.append(float(token.replace(SIGN_NUMBER_MINUS, '-')))
            else:
                operand1 = stack.pop()
                # Temp implementation.
                # TODO: improve. avoid messy if-elif-else struct.
                if token in UNARY_OPERATORS_DICT:
                    unary_result = UNARY_OPERATORS_DICT.get(token).solve(operand1)
                    stack.append(unary_result)
                elif token in BINARY_OPERATORS_DICT:
                    operand2 = stack.pop()
                    binary_result = BINARY_OPERATORS_DICT.get(token).solve(operand2, operand1)
                    stack.append(binary_result)
        self._result = stack[0] if stack  else "Nothing to calculate."