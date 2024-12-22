"""
Module for processing string.
Contains an abstract base class and an arithmetic implementation.
"""

from abc import ABC, abstractmethod

from calculator.logic.exceptions import EmptyEquationError
from calculator.utils import general_utils


class StringProcessor(ABC):
    """
    Abstract class for processing a string.
    """

    @abstractmethod
    def __init__(self, string: str):
        """
        Abstract init method for StringProcessor.

        :param string: string which needs to be processed.
        :type string: str
        """

    @abstractmethod
    def process(self, string: str):
        """
        Abstract method for processing a string.
        Determines the order of the process logic.

        :param string: String to process.
        :type string: str
        """


class ArithmeticStringProcessor(StringProcessor):
    """
    Class for arithmetic processing of user's input.
    Processes and formats user input equations.
    Validates and removes whitespace, and checks for empty input.
    """

    def __init__(self, string: str = None):
        """
        Process (reformat) users' input.

        :param string: The equation provided by the user.
            If not provided, defaults to None.
        :type string: str
        """

        self._equation = string

    def process(self, string: str) -> str:
        """
        Determines the order of the process logic.
        Processes (fixes format) of user's input.
        Redefines equation.

        :return: Processed user's input (equation with fixed format).
        :rtype: str
        """

        self._equation = string
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
        Validates that user's input is not empty after removal of white spaces.
        :raises EmptyEquationError: if processed equation is empty.
        """

        if self._equation == '':
            raise EmptyEquationError()
