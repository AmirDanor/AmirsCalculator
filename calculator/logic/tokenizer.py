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
    Class for arithmetic equations tokenization.
    """

    def tokenize(self, equation: str) -> list:
        """
        Tokenizes basic arithmetic equations into a list of _tokens.

        :param equation: arithmetic equation.
        :type equation: str
        :return: tokenized arithmetic equation.
        :rtype: list
        """

        tokens: [str] = []
        number = general_utils.EMPTY_STR
        for char in equation:
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
