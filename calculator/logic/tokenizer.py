"""
Module for tokenizing string into list.
Contains an abstract base class and an arithmetic implementation.
"""

from abc import ABC, abstractmethod

from calculator.utils import general_utils


class Tokenizer(ABC):
    """
    Abstract class for tokenizing str.
    """

    @abstractmethod
    def tokenize(self, string: str) -> list:
        """
        Abstract method for tokenizing a string.
        """


class ArithmeticTokenizer(Tokenizer):
    """
    Class for string arithmetic equation tokenization.
    """

    def tokenize(self, string: str) -> list:
        """
        Tokenizes basic arithmetic string into a list of _tokens.

        :param string: arithmetic equation.
        :type string: str
        :return: tokenized arithmetic equation.
        :rtype: list
        """

        tokens: [str] = []
        number = general_utils.EMPTY_STR
        for char in string:
            if char.isdigit() or char == general_utils.DOT:
                number += char
            else:
                if number:
                    tokens.append(number)
                    number = general_utils.EMPTY_STR
                if char.strip():  # Ignore whitespace
                    tokens.append(char)
        if number:
            tokens.append(number)
        return tokens
