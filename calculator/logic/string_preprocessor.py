from calculator.logic.exceptions import UnmatchedOpeningParenthesesError, \
    UnmatchedClosingParenthesesError
from calculator.utils import general_utils


class StringPreprocessor:
    def __init__(self, equation: str):
        """
        Preprocess users' input (find error before processing)

        :param equation: User's input (equation)
        :type equation: str
        """
        self._equation = equation

    def preprocess(self):
        self.validate_parentheses()

    def validate_parentheses(self):
        """
        Validate parentheses are correctly matched and no empty parentheses exist.

        :return: List of indices where '(' appears in the equation
        :rtype: list
        """
        opening_indices = []  # Indexes of opening parentheses
        stack = []  # Tracks opening parentheses
        for index in range(len(self._equation)):
            char = self._equation[index]
            if char == general_utils.OPEN_BRACKETS:
                opening_indices.append(index)
                stack.append(index)
            elif char == general_utils.CLOSE_BRACKETS:
                if stack:
                    stack.pop()
                else:
                    raise UnmatchedClosingParenthesesError(index)

        if stack:  # If there are any unmatched opening parentheses
            raise UnmatchedOpeningParenthesesError(stack[0])
