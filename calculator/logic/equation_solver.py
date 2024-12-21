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
        self._infix_to_postfix()
        self._solve_postfix()
        return self._result

    def _infix_to_postfix(self):
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
                self._unary_operator_to_postfix(token, index, stack, postfix)
            elif token == general_utils.OPEN_BRACKETS:
                stack.append(token)
            elif token == general_utils.CLOSE_BRACKETS:
                self._close_bracket_to_postfix(token, index, stack, postfix)
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

    def _unary_operator_to_postfix(self, token: str, index: int, stack: list,
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

    def _close_bracket_to_postfix(self, token: str, index: int, stack: list,
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

    def _operator_to_postfix(self, token: str, index: int, stack: list,
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

    def _solve_postfix(self):
        """
        Solves the equation represented by postfix stack and updates the
        _result.
        """
        stack = []
        for token in self._postfix_stack:
            if (operand_utils.is_operand(token)
                    or operator_utils.SIGN_MINUS_SYMBOL in token):
                # Operand
                fixed_token = token.replace(operator_utils.SIGN_MINUS_SYMBOL,
                                            operator_utils.SUB_SYMBOL)
                try:
                    token_as_number = float(fixed_token)
                except ValueError as ve:
                    print("line 153 in equation_solver.py")
                    print(ve)
                    return None
                stack.append(token_as_number)
            else:  # Operator
                try:
                    operand1 = stack.pop()
                except IndexError:  # todo: maybe check in a separate func
                    if token in UNARY_OPERATORS_DICT:
                        raise OperatorUsageError(token, "No operand")
                    else:
                        raise OperatorUsageError(token, "No operands")
                # Temp implementation.
                if token in UNARY_OPERATORS_DICT:
                    unary_result = UNARY_OPERATORS_DICT.get(token).solve(
                        operand1)
                    stack.append(unary_result)
                elif token in BINARY_OPERATORS_DICT:
                    try:
                        operand2 = stack.pop()
                    except IndexError:  # todo: maybe check in a separate func
                        raise OperatorUsageError(token,
                                                 "Missing operand")
                    binary_result = BINARY_OPERATORS_DICT.get(token).solve(
                        operand2, operand1)
                    stack.append(binary_result)
        if len(stack) >= 2:
            self._result = "Wrong usage of parentheses"  # todo: change str
        else:
            self._result = stack[0] if stack else "Nothing to calculate."
