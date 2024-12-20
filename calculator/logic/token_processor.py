# todo: disable 1234. support

from abc import ABC, abstractmethod

from calculator.logic.exceptions import UnaryError, \
    MultipleDotsError, MultipleDotsOperandError, \
    SingleDotError
from calculator.utils import operand_utils, operator_utils, general_utils
from calculator.utils.operator_registry import OperatorRegistry

OPERATOR_REGISTRY = OperatorRegistry()
UNARY_OPERATORS_DICT = OPERATOR_REGISTRY.get_unary_operators()
BINARY_OPERATORS_DICT = OPERATOR_REGISTRY.get_binary_operators()
# Merges both dictionaries into a single dictionary
OPERATORS_DICT = {**UNARY_OPERATORS_DICT,
                  **BINARY_OPERATORS_DICT}
RIGHT_UNARY_OPERATORS_DICT = OPERATOR_REGISTRY.get_right_unary_operators()
LEFT_UNARY_OPERATORS_DICT = OPERATOR_REGISTRY.get_left_unary_operators()


class TokenProcessor(ABC):
    """
    Abstract class for tokenized list processor.
    """

    @abstractmethod
    def __init__(self, tokens: list):
        """
        Abstract init method.
        :param tokens: tokens which needs to be processed
        :type tokens: list
        """

    @abstractmethod
    def process(self, tokens: list) -> list:
        """
        Abstract method for processing a list of tokens.
        :param tokens: tokenized sequence
        :type tokens: list
        :return: processed list of tokens
        :rtype: list
        """


class ArithmeticTokenProcessor(TokenProcessor):
    """
    Class for processing arithmetic tokenized list.
    """

    def __init__(self, tokens: list = None):
        if tokens is None:
            tokens = []  # Default to an empty list if no tokens are provided
        self._tokens = tokens

    def process(self, tokens: list = None) -> list:
        if tokens is not None:
            self._tokens = tokens
        self.handle_dots()
        self.delete_extra_minuses()
        self.join_sign_minuses()
        self.replace_unary_minuses()
        self.validate()
        return self._tokens

    def handle_dots(self):
        """
        Validates tokens which include dots, raises exceptions if needed.
        """

        for token in self._tokens:
            if token == general_utils.DOT:
                raise SingleDotError()
            dot_count = token.count(general_utils.DOT)
            if token.count(general_utils.DOT) > 1:
                if not any(char.isdigit() for char in token):
                    raise MultipleDotsError(dot_count)
                raise MultipleDotsOperandError(token, dot_count)

    def delete_extra_minuses(
            self):  # TODO: check theres a maximum one . (dot) in operand.
        """
        Delete multiple appearances of minus in a row from self._tokens.
        After end of function, there are no more than 2 minuses in a row in
        self._tokens.
        """

        tokens = []
        number = ''
        for index in range(len(self._tokens) - 2, 0, -1):
            if (self._tokens[index] == operator_utils.SUB_SYMBOL and
                    self._tokens[index - 1] == operator_utils.SUB_SYMBOL):
                # Check for context: number/bracket to the right, operator
                # to the left
                if ((operand_utils.is_operand(self._tokens[index + 1]) or
                     self._tokens[
                         index + 1] == general_utils.OPEN_BRACKETS) and
                        (index - 2 < 0 or self._tokens[
                            index - 2] in BINARY_OPERATORS_DICT or
                         self._tokens[
                             index - 2] in LEFT_UNARY_OPERATORS_DICT or
                         self._tokens[
                             index - 2] == general_utils.OPEN_BRACKETS)):
                    # Remove the two minuses
                    del self._tokens[index]
                    del self._tokens[index - 1]
                    index -= 1

    def join_sign_minuses(self):
        """
        Joins sign minuses directly to numbers.
        """

        for index in range(1, len(self._tokens) - 1, 1):
            if (self._tokens[index] == operator_utils.SUB_SYMBOL
                    and (self.prev_token_is_a_non_minus_valid_operand(index)
                         or self.prev_token_is_a_valid_minus_operand(index))):
                if general_utils.OPEN_BRACKETS == self._tokens[index + 1]:
                    # NOTE: replaced in with ==
                    #  If an opening bracket comes after current unary minus
                    self.minus_brackets_handle(index)
                else:
                    self._tokens[index + 1] = (operator_utils.SIGN_MINUS_SYMBOL
                                               + self._tokens[index + 1])
                    del self._tokens[index]
                    index -= 1

    def prev_token_is_a_non_minus_valid_operand(self, index: int) -> bool:
        """
        checks if previous token is valid to appear before a sign minus
        (other than a minus)
        :param index: index of relevant token in tokens list
        :type index: str
        :return: if previous token is a valid to appear before a sign minus
        :rtype: bool
        """

        prev_token = self._tokens[index - 1]
        return ((prev_token in BINARY_OPERATORS_DICT or
                 prev_token in LEFT_UNARY_OPERATORS_DICT)
                and prev_token != operator_utils.SUB_SYMBOL)

    def prev_token_is_a_valid_minus_operand(self, index: int) -> bool:
        """
        checks if previous token is a minus, and if the token before that,
        makes the token in current index a sign minus
        :param index: index of relevant token in tokens list
        :type index: str
        :return: if previous token is a minus, and if the token before that,
            makes the token in current index a sign minus
        :rtype: bool
        """

        return (self._tokens[index - 1] ==
                operator_utils.SUB_SYMBOL
                and index - 2 >= 0
                and (self._tokens[index - 2].isdigit()
                     or general_utils.DOT in self._tokens[
                         index - 2]
                     or operator_utils.SIGN_MINUS_SYMBOL in
                     self._tokens[index - 2]
                     or general_utils.CLOSE_BRACKETS ==
                     self._tokens[index - 2]
                     or self._tokens[index - 2]
                     in RIGHT_UNARY_OPERATORS_DICT))

    def minus_brackets_handle(self, index: int):  # Assuming brackets are valid
        """
        :param index: index of minus in self._tokens
        :type index: int
        """

        self._tokens.insert(index, general_utils.OPEN_BRACKETS)
        index += 3
        track_brackets = [general_utils.OPEN_BRACKETS]
        while track_brackets:
            if self._tokens[index] == general_utils.OPEN_BRACKETS:
                track_brackets.append(general_utils.OPEN_BRACKETS)
            if self._tokens[index] == general_utils.CLOSE_BRACKETS:
                if track_brackets:
                    self._tokens.insert(index, general_utils.CLOSE_BRACKETS)
                    return
                else:
                    track_brackets.pop()
            index += 1

    def replace_unary_minuses(self):
        """
        Replaces all appearances of unary minuses with SIGN_UNARY_MINUS [';']
        """

        for index in range(0, len(self._tokens) - 1, 1):
            if self._tokens[index] == '-' and (
                    index == 0 or
                    general_utils.OPEN_BRACKETS in self._tokens[index - 1]):
                self._tokens[index] = operator_utils.UNARY_MINUS_SYMBOL

    def validate(self):
        """
        Checks for errors in tokenized equation.
        """

        index = 0
        for token in self._tokens:
            if token in UNARY_OPERATORS_DICT:
                self.validate_unary_operator(token, index)
            index += 1

    def validate_unary_operator(self, token: str, index: int):
        """
        Validates unary operator as part of equation
        :param token: unary operator's symbol
        :type token: str
        :param index: index of current token in tokens list
        :type index: int
        """

        if OPERATOR_REGISTRY.is_left_unary_operator(
                token):  # Left unary operator
            self.validate_left_unary_operator(token, index)
        else:  # Right unary operator
            self.validate_right_unary_operator(token, index)

    def validate_left_unary_operator(self, token, index):
        """
        Validates left unary operator as part of equation
        :param token: left unary operator's symbol
        :type token: str
        :param index: index of current token in tokens list
        :type index: int
        :raises UnaryError: if operator's usage is not valid
        """

        if (index > 0  # Check token to the left
                and self._tokens[index - 1] not in BINARY_OPERATORS_DICT
                and self._tokens[index - 1] != general_utils.OPEN_BRACKETS):
            raise UnaryError(token)
        if (index < len(self._tokens) - 1  # Check token to the right
                and (not operand_utils.is_operand(self._tokens[index + 1])
                     and self._tokens[
                         index + 1] != general_utils.OPEN_BRACKETS)):
            raise UnaryError(token)

    def validate_right_unary_operator(self, token, index):
        """
        Validates right unary operator as part of equation
        :param token: right unary operator's symbol
        :type token: str
        :param index: index of current token in tokens list
        :type index: int
        :raises UnaryError:if operator's usage is not valid
        """

        if (index > 0  # Check token to the left
                and not operand_utils.is_operand(self._tokens[index - 1])
                and self._tokens[index - 1] not in
                operator_utils.ALLOWED_BEFORE_RIGHT_UNARY):
            # raise UnaryError(token, "left")
            raise UnaryError(token)
        if (index < len(self._tokens) - 1  # Check token to the right
                and self._tokens[index + 1]
                not in operator_utils.ALLOWED_AFTER_RIGHT_UNARY):
            raise UnaryError(token)
