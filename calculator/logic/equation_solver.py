"""
Module purpose is to store class which is responsible for equation-solving.
"""
from calculator.logic.exceptions import OperatorUsageError, \
    WrongParenthesesUsageError, ExpectedOperandError
from calculator.utils import operator_utils, operand_utils, general_utils, \
    operators
from calculator.utils.operator_registry import OperatorRegistry
OPERATOR_REGISTRY = OperatorRegistry()
# Merges both dictionaries into a single dictionary


class EquationSolver:
    """
    Class responsible for solving math equation.
    It uses a postfix-notation approach to solve the equation.
    Converts an infix equation to postfix, then evaluates the result.
    """
    def __init__(self, equation: list):
        """
        Initializes a tokenized equation.

        :param equation: A list of tokens representing a mathematical equation.
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
            elif token is operators.UnaryOperator:
                self._unary_operator_to_postfix(token, index, stack, postfix)
            elif token == general_utils.OPEN_BRACKETS:
                stack.append(token)
            elif token == general_utils.CLOSE_BRACKETS:
                self._close_bracket_to_postfix(index, stack, postfix)
            else:  # Operator
                while (stack and stack[-1]
                       != general_utils.OPEN_BRACKETS
                       and OPERATOR_REGISTRY.get_precedence(
                            token) <= OPERATOR_REGISTRY.get_precedence(
                            stack[-1])):
                    postfix.append(stack.pop())
                stack.append(token)
            index += 1

        while stack:
            postfix.append(stack.pop())

        self._postfix_stack = postfix

    def _unary_operator_to_postfix(self, token: str, index: int, stack: list,
                                   postfix: list):
        """
        Handles unary operators when converting infix equation to postfix.

        :param token: symbol of operator
        :type token: str
        :param index: index of current token in self._tokens
        :type index: int
        :param stack: The stack used for infix-to-postfix equation convertion.
        :type stack: list
        :param postfix: Postfix representation of equation.
        :type postfix: list
        """

        if token in operator_utils.LEFT_UNARY_OPERATORS:
            # Push left-sided unary operator
            stack.append(token)
        else:  # Right-sided unary operators
            if index > 0 and operand_utils.is_operand(
                    self._tokens[index - 1]):
                postfix.append(token)
            else:
                stack.append(token)

    def _close_bracket_to_postfix(self, index: int, stack: list,
                                  postfix: list):
        """
        Handles closing brackets when converting infix equation to postfix.

        :param index: The index of current token in the equation.
        :type index: int
        :param stack: The stack used for infix-to-postfix equation convertion.
        :type stack: list
        :param postfix: Postfix representation of equation.
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
        Handles operators when converting infix equation to postfix.

        :param token: The symbol of operator to handle.
        :type token: str
        :param index: The index of current token in the equation.
        :type index: int
        :param stack: The stack used for infix-to-postfix equation convertion.
        :type stack: list
        :param postfix: Postfix representation of equation.
        :type postfix: list
        """

        while (stack and stack[-1]
               != general_utils.OPEN_BRACKETS
               and OPERATOR_REGISTRY.get_precedence(
                    token) <= OPERATOR_REGISTRY.get_precedence(
                    stack[-1])):
            postfix.append(stack.pop())
        stack.append(token)

    def _solve_postfix(self):
        """
        Solves the equation represented by postfix stack and updates the
            _result.

        :raises OperatorUsageError: If misused operators exist.
        :raises WrongParenthesesUsageError: if equations contains wrong
            parentheses usage.
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
                except ValueError:
                    raise ExpectedOperandError(fixed_token)
                stack.append(token_as_number)
            else:  # Operator
                try:
                    operand1 = stack.pop()
                except IndexError:  # todo: maybe check in a separate func
                    if token in operator_utils.ALL_UNARY_OPERATORS:
                        raise OperatorUsageError(token, "No operand")
                    else:
                        raise OperatorUsageError(token, "No operands")
                # Temp implementation.
                if token in operator_utils.ALL_UNARY_OPERATORS:
                    unary_result = (OPERATOR_REGISTRY.get_unary_operators()
                                    .get(token).solve(operand1))
                    stack.append(unary_result)
                elif token in operator_utils.BINARY_OPERATORS:
                    try:
                        operand2 = stack.pop()
                    except IndexError:  # todo: maybe check in a separate func
                        raise OperatorUsageError(token,
                                                 "Missing operand")
                    binary_result = (OPERATOR_REGISTRY.get_binary_operators()
                                     .get(token).solve(operand2, operand1))
                    stack.append(binary_result)
        if len(stack) >= 2:
            raise WrongParenthesesUsageError()
        else:
            self._result = stack[0] if stack else "Nothing to calculate."
