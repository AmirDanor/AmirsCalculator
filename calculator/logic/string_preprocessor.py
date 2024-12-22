"""
Module contains StringPreprocessor which ensures user's input
consists of valid chars only, and contains only valid parentheses.
"""

from calculator.logic.exceptions import UnmatchedOpeningParenthesesError, \
    UnmatchedClosingParenthesesError, EmptyParenthesesError, InvalidInputError
from calculator.utils import general_utils


class StringPreprocessor:
    """
    Class to make sure string is valid before start of procession.
    Ensures that the user's input consists of valid characters only and
    contains only valid parentheses.
    """

    def __init__(self, equation: str):
        """
        Preprocess users' input (find error before processing)

        :param equation: User's input (equation)
        :type equation: str
        """

        self._equation = equation

    def preprocess(self):
        """
        Determines the order of the pre-process logic.
        Validates the user's input by performing string-based tests:
        checks for invalid characters and parentheses.
        """

        self._validate_input()
        self._validate_parentheses()

    def _validate_input(self):
        """
        Checks if there are forbidden chars in the user input

        :return: Whether equation contains
            forbidden chars or not
        :rtype: bool
        :raises InvalidInputError: if input contains forbidden chars
        """

        if not set(self._equation).issubset(
                general_utils.VALID_INPUT_CHARACTERS):
            raise InvalidInputError(self._equation)

    def _validate_parentheses(self):
        """
        Validate parentheses are correctly matched and no empty parentheses
            exist

        :raises EmptyParenthesesError: if empty parentheses found
        :raises UnmatchedClosingParenthesesError: if unmatched closing
            parentheses found
        :raises UnmatchedOpeningParenthesesError: if unmatched opening
            parentheses found
        """

        stack = []  # Tracks opening parentheses ny index
        is_empty = False
        for index in range(len(self._equation)):
            char = self._equation[index]
            if char == general_utils.OPEN_BRACKETS:
                is_empty = True
                stack.append(index)
            elif char == general_utils.CLOSE_BRACKETS:
                if stack:
                    if is_empty:
                        raise EmptyParenthesesError(stack.pop(), index)
                    stack.pop()
                    is_empty = False
                else:
                    raise UnmatchedClosingParenthesesError(index)
            elif char not in general_utils.EMPTY_CHARACTERS:
                is_empty = False

        if stack:  # If there are any unmatched opening parentheses
            raise UnmatchedOpeningParenthesesError(stack[0])
