from calculator.logic.exceptions import OperatorUsageError
from calculator.utils import operator_utils, operand_utils, general_utils
from calculator.utils.operator_registry import OperatorRegistry
from calculator.utils.operators import UnaryOperator

OPERATOR_REGISTRY = OperatorRegistry()
UNARY_OPERATORS_DICT = OPERATOR_REGISTRY.get_unary_operators()
BINARY_OPERATORS_DICT = OPERATOR_REGISTRY.get_binary_operators()
# Merges both dictionaries into a single dictionary
operators_dict = {**UNARY_OPERATORS_DICT,
                  **BINARY_OPERATORS_DICT}


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
            if operand_utils.is_operand(token):  # Operand
                #  removed: or operator_utils.SIGN_MINUS_SYMBOL in token
                postfix.append(token)
            elif token is UnaryOperator:
                self.unary_operator_to_postfix(token, index, stack, postfix)
            elif token == general_utils.OPEN_BRACKETS:
                stack.append(token)
            elif token == general_utils.CLOSE_BRACKETS:
                self.close_bracket_to_postfix(token, index, stack, postfix)
            else:  # Operator
                while (stack and stack[-1]
                       != general_utils.OPEN_BRACKETS
                       and OPERATOR_REGISTRY.get_precedence(
                            token) <= OPERATOR_REGISTRY.get_precedence(
                            stack[-1])):  # add '-('
                    postfix.append(stack.pop())
                stack.append(token)
            index += 1

        while stack:
            postfix.append(stack.pop())

        self._postfix_stack = postfix

    def unary_operator_to_postfix(self, token: str, index: int, stack: list,
                                  postfix: list):
        """
        handles unary operators when converting infix equation to postfix
        :param token: symbol of operator
        :type token: str
        :param index: index of current token in self._tokens
        :type index: int
        :param stack: stack for equation convertion
        :type stack: list
        :param postfix: postfix representation of equation
        :type postfix: list
        """

        if OPERATOR_REGISTRY.is_left_unary_operator(token):
            # Push left-sided unary operator
            stack.append(token)
        else:  # Right-sided unary operators
            if index > 0 and operand_utils.is_operand(
                    self._tokens[index - 1]):
                postfix.append(token)
            else:
                stack.append(token)

    def close_bracket_to_postfix(self, token: str, index: int, stack: list,
                                 postfix: list):
        """
        handles closing brackets when converting infix equation to postfix
        :param token: symbol of closing bracket
        :type token: str
        :param index: index of current token in self._tokens
        :type index: int
        :param stack: stack for equation convertion
        :type stack: list
        :param postfix: postfix representation of equation
        :type postfix: list
        """

        while (stack[-1] != general_utils.OPEN_BRACKETS and stack[-1]
               != operator_utils.SIGN_MINUS_SYMBOL
               + general_utils.OPEN_BRACKETS):
            postfix.append(stack.pop())
        stack.pop()

    def operator_to_postfix(self, token: str, index: int, stack: list,
                            postfix: list):
        """
        handles operators when converting infix equation to postfix
        :param token: symbol of operator
        :type token: str
        :param index: index of current token in self._tokens
        :type index: int
        :param stack: stack for equation convertion
        :type stack: list
        :param postfix: postfix representation of equation
        :type postfix: list
        """

        while (stack and stack[-1]
               != general_utils.OPEN_BRACKETS
               and OPERATOR_REGISTRY.get_precedence(
                    token) <= OPERATOR_REGISTRY.get_precedence(
                    stack[-1])):  # add '-('
            postfix.append(stack.pop())
        stack.append(token)

    def solve_postfix(self):
        """
        Solves the equation represented by postfix stack and updates the
        _result.
        """
        stack = []
        for token in self._postfix_stack:
            if operand_utils.is_operand(
                    token) or operator_utils.SIGN_MINUS_SYMBOL in token:
                # Operand
                fixed_token = token.replace(operator_utils.SIGN_MINUS_SYMBOL,
                                            operator_utils.SUB_SYMBOL)
                try:
                    token_as_number = float(fixed_token)
                    stack.append(token_as_number)
                except ValueError as ve:
                    print(ve)
                    return None
            else:  # Operator
                try:
                    operand1 = stack.pop()
                except IndexError:  # todo: maybe check in a separate func
                    raise OperatorUsageError(token)
                    return None
                # Temp implementation.
                if token in UNARY_OPERATORS_DICT:
                    unary_result = UNARY_OPERATORS_DICT.get(token).solve(
                        operand1)
                    stack.append(unary_result)
                elif token in BINARY_OPERATORS_DICT:
                    try:
                        operand2 = stack.pop()
                    except IndexError:  # todo: maybe check in a separate func
                        raise OperatorUsageError(token)
                        return None
                    binary_result = BINARY_OPERATORS_DICT.get(token).solve(
                        operand2, operand1)
                    stack.append(binary_result)
        if len(stack) >= 2:
            self._result = "Wrong usage of parentheses"  # todo: change str
        else:
            self._result = stack[0] if stack else "Nothing to calculate."
