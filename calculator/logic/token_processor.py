from abc import ABC, abstractmethod

from calculator.logic.exceptions import UnaryError, EmptyParenthesesError
from calculator.utils.operator_registry import OperatorRegistry
from calculator.utils.operand_utils import SIGN_NUMBER_MINUS, SIGN_UNARY_MINUS, is_operand, ALLOWED_BEFORE_RIGHT_UNARY, \
    ALLOWED_AFTER_RIGHT_UNARY

OPERATOR_REGISTRY = OperatorRegistry()
UNARY_OPERATORS_DICT = OPERATOR_REGISTRY.get_unary_operators()
BINARY_OPERATORS_DICT = OPERATOR_REGISTRY.get_binary_operators()
OPERATORS_DICT = {**UNARY_OPERATORS_DICT, **BINARY_OPERATORS_DICT} # Merges both dictionaries into a single dictionary
RIGHT_UNARY_OPERATORTS_DICT = OPERATOR_REGISTRY.get_right_unary_operators()

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
    def process(self) -> list:
        """
        Abstract method for processing a list of _tokens.
        :return: processed list of _tokens
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
        if tokens != None:
            self._tokens = tokens
        self.delete_extra_minuses()
        self.join_number_minuses()
        self.replace_unary_minuses()
        self.validate()
        return self._tokens

    def delete_extra_minuses(self): # TODO: check theres a maximum one . (dot) in operand.
        """
        Delete multiple appearances of minus in a row from self._tokens.
        After end of function, there are no more than 2 minuses in a row in self._tokens.
        """
        tokens = []
        number = ''
        for index in range (len(self._tokens) - 2, 0, -1): #Make sure vars are correct... -2... 0...
            if self._tokens[index] == '-' and self._tokens[index - 1] == '-':
                # Check for context: number/bracket to the right, operator to the left
                if  ((is_operand(self._tokens[index + 1]) or self._tokens[index + 1] == '(') and
                        (index - 2 < 0 or self._tokens[index - 2] in BINARY_OPERATORS_DICT or self._tokens[index - 2] == '(')):
                    # Remove the two minuses
                    del self._tokens[index]
                    del self._tokens[index - 1]
                    index -= 1
        # print(f" after delete_extra_unary_minuses: {self._tokens}") # For testing


    def join_number_minuses(self):
        """
        Joins number minuses directly to numbers.
        """
        for index in range(1, len(self._tokens) - 1, 1):
            if (self._tokens[index] == '-'  # TODO: Simplify this complicated statement
                    and ((self._tokens[index - 1] in BINARY_OPERATORS_DICT
                          and self._tokens[index - 1] != '-')
                         or (self._tokens[index - 1] == '-'
                             and index - 2 >= 0
                             and (self._tokens[index - 2].isdigit() #TODO: place in module
                                  or '.' in self._tokens[index - 2]
                                  or '_' in self._tokens[index - 2]
                                  or ')' == self._tokens[index - 2]
                                  or self._tokens[index - 2] in RIGHT_UNARY_OPERATORTS_DICT)))):
                if ('(' in self._tokens[index + 1]):
                    self.minus_brackets_handle(index)
                else:
                    self._tokens[index + 1] = SIGN_NUMBER_MINUS + self._tokens[index + 1]
                    del self._tokens[index]
                    index -= 1 # not sure...
        # print(f" after join_number_minuses: {self._tokens}")  # For testing

    def minus_brackets_handle(self, index: int): # Assuming brackets are valid
        """
        :param index: index of minus in self._tokens
        :type index: int
        """
        self._tokens.insert(index, '(')
        # print(f"og: {self._tokens}")
        index+=3
        # print(f"in index: {index} = {self._tokens[index]}")
        track_brackets = ['(']
        while track_brackets:
            # print(f"tracking: {track_brackets}")
            if (self._tokens[index] == '('):
                track_brackets.append('(')
            if (self._tokens[index] == ')'):
                if track_brackets:
                    self._tokens.insert(index, ')')
                    return
                else:
                    track_brackets.pop()
            index+=1

    def replace_unary_minuses(self):
        """
        Replaces all appearances of unary minuses with SIGN_UNARY_MINUS [';']
        """
        for index in range(0, len(self._tokens) - 1, 1):
            if self._tokens[index] == '-' and (index == 0 or '(' in self._tokens[index - 1]):
                self._tokens[index] = SIGN_UNARY_MINUS
        # print(f" after replace_unary_minus: {self._tokens}")  # For testing

    def validate(self):
        """
        Checks for errors in tokenized equation.
        """ # add info about exception it raises and when it is being raised
        index = 0
        for token in self._tokens:
            if token in UNARY_OPERATORS_DICT:
                if OPERATOR_REGISTRY.is_left_unary_operator(token):  # Left unary operator
                    if (index > 0  # Check token to the left
                            and self._tokens[index-1] not in BINARY_OPERATORS_DICT
                            and self._tokens[index-1] != '('):
                        #print(f"before: {index}")
                        raise UnaryError(token)
                    if (index < len(self._tokens) - 1 # Check token to the right
                            and (not is_operand(self._tokens[index + 1])
                                 and self._tokens[index + 1] != '(')):
                        #print(f"after: {index}")
                        raise UnaryError(token)
                else: # Right unary operator
                    if (index > 0 # Check token to the left
                            and not is_operand(self._tokens[index-1])
                            and self._tokens[index-1] not in ALLOWED_BEFORE_RIGHT_UNARY):
                        #print(f"before: {index}")
                        raise UnaryError(token)
                    if (index < len(self._tokens) - 1 # Check token to the right
                            and self._tokens[index+1] not in ALLOWED_AFTER_RIGHT_UNARY):
                        #print(f"after: {index}")
                        raise UnaryError(token)
            elif token == '(':
                if index < len(self._tokens) - 1 and self._tokens[index+1] == ')':
                    raise EmptyParenthesesError()
            index += 1