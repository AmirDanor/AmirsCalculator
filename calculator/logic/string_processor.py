from calculator.logic.exceptions import EmptyEquationError
from calculator.utils import general_utils


class StringProcessor:
    def __init__(self, equation: str):
        """
        Process (reformat) users' input.

        :param equation: User's input (equation)
        :type equation: str
        """
        self._equation = equation

    def process(self):
        """
        Process (fix format) of user's input.

        :return: Processed user's input (equation with fixed format)
        :rtype: str
        """
        self._remove_white_spaces()
        self._not_empty_validator()
        return self._equation

    def _remove_white_spaces(self):
        """
        Removes white spaces from str equation.
        """
        self._equation = ''.join(c for c in self._equation if
                                 c not in general_utils.EMPTY_CHARACTERS)

    def _not_empty_validator(self):
        """
        Validates that user's input is not empty after removal of white spaces
        :throws EmptyEquationError: if processed equation is empty
        """
        if self._equation == '':
            raise EmptyEquationError()
