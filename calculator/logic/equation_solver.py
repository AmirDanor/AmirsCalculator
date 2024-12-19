from calculator.utils import operator_utils, operand_utils, general_utils
from calculator.utils.operator_registry import OperatorRegistry
from calculator.utils.operators import UnaryOperator

OPERATOR_REGISTRY = OperatorRegistry()
UNARY_OPERATORS_DICT = OPERATOR_REGISTRY.get_unary_operators()
BINARY_OPERATORS_DICT = OPERATOR_REGISTRY.get_binary_operators()
operators_dict = {**UNARY_OPERATORS_DICT,
                  **BINARY_OPERATORS_DICT}  # Merges both dictionaries into a single dictionary


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
        self.infix_to_postfix()
        self.solve_postfix()
        # if self._result == -0.0:
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
            if operand_utils.is_operand(
                    token) or operator_utils.NUMBER_MINUS in token:  # Operand
                postfix.append(token)
            elif token is UnaryOperator:
                if OPERATOR_REGISTRY.is_left_unary_operator(
                        token):  # Push left-sided unary operator
                    stack.append(token)
                else:  # Right-sided unary operators
                    if index > 0 and operand_utils.is_operand(
                            self._tokens[index - 1]):
                        postfix.append(token)
                    else:
                        stack.append(token)
            elif token == general_utils.OPEN_BRACKETS:
                stack.append(token)
            elif token == general_utils.CLOSE_BRACKETS:
                while stack[-1] != general_utils.OPEN_BRACKETS and stack[
                    -1] != operator_utils.NUMBER_MINUS + general_utils.OPEN_BRACKETS:
                    postfix.append(stack.pop())
                if stack[
                    -1] != operator_utils.NUMBER_MINUS + general_utils.OPEN_BRACKETS:
                    pass  # Insert negative value of _result in brackets...
                stack.pop()
            else:  # Operator
                while stack and stack[
                    -1] != general_utils.OPEN_BRACKETS and operand_utils.precedence(
                        token) <= operand_utils.precedence(
                        stack[-1]):  # add '-('
                    postfix.append(stack.pop())
                stack.append(token)
            index += 1

        while stack:
            postfix.append(stack.pop())

        self._postfix_stack = postfix
        # print(f"Postfix stack: {self._postfix_stack}")  # For testing

    def solve_postfix(self):
        """
        Solves the equation represented by postfix stack and updates the _result.
        """
        stack = []
        for token in self._postfix_stack:
            if operand_utils.is_operand(
                    token) or operator_utils.NUMBER_MINUS in token:  # Operand
                fixed_token = token.replace(operator_utils.NUMBER_MINUS,
                                            operator_utils.MINUS)
                try:
                    token_as_number = float(fixed_token)
                    stack.append(token_as_number)
                except ValueError as ve:
                    print(ve)
                    return None
            else:
                # try:
                operand1 = stack.pop()
                # except IndexError as ie:
                #    print(ie)
                #    return None
                # Temp implementation.
                # TODO: improve. avoid messy if-elif-else struct.
                if token in UNARY_OPERATORS_DICT:
                    unary_result = UNARY_OPERATORS_DICT.get(token).solve(
                        operand1)
                    stack.append(unary_result)
                elif token in BINARY_OPERATORS_DICT:
                    operand2 = stack.pop()
                    binary_result = BINARY_OPERATORS_DICT.get(token).solve(
                        operand2, operand1)
                    stack.append(binary_result)
        if len(stack) >= 2:
            self._result = "Wrong usage of parentheses"  # todo: change str
        else:
            self._result = stack[0] if stack else "Nothing to calculate."
