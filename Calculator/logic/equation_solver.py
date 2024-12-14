# File contains prints for dev tests
from Calculator.logic.operator_registry import OperatorRegistry
from Calculator.logic.operators import UnaryOperator

SIGN_NUMBER_MINUS = '_'
SIGN_UNARY_MINUS = ';'

operator_registery = OperatorRegistry()
unary_operators_dict = operator_registery.get_unary_operators()
binary_operators_dict = operator_registery.get_binary_operators()
operators_dict = {**unary_operators_dict, **binary_operators_dict} # Merges both dictionaries into a single dictionary

class EquationSolver:
    def __init__(self, equation: str):
        """
        Solves the equation.

        :param equation: User's input.
        :type equation: str
        """
        self.equation = equation
        self.tokens = []
        self.postfix_stack = []
        self.result = None

    def solve(self):
        """
        Solves the equation by calling the class' functions.

        :return: Solution to equation
        :rtype: float
        """
        self.tokenize()
        self.delete_extra_minuses()
        self.join_number_minuses()
        self.replace_unary_minuses()
        self.infix_to_postfix()
        self.solve_postfix()
        if self.result == -0.0:
            self.result = 0.0
        return self.result


    def precedence(self, operator):
        """
        :param operator: representation of operator
        :type operator: str
        :return: operator's precedence
        :rtype: int
        """
        return operator_registery.get_precedence_for_operator(operator)

    def is_operand(self, string: str) -> bool:
        return string.isdigit() or '.' in string

    def tokenize(self): # TODO: check theres a maximum one . (dot) in operand.
        """
        Converts the str equation into a list of tokens.
        """
        tokens = []
        number = ''
        for character in self.equation:
            if character.isdigit() or character == '.':
                number += character
            else:
                if number != '':
                    tokens.append(number)
                    number = ''
                if character in operators_dict or character in '()':
                    tokens.append(character)
        if number != '':
            tokens.append(number)
        self.tokens = tokens
        # print(self.tokens) # For testing

    def delete_extra_minuses(self): # TODO: check theres a maximum one . (dot) in operand.
        """
        Delete multiple appearances of minus in a row from self.tokens.
        After end of function, there are no more than 2 minuses in a row in self.tokens.
        """
        tokens = []
        number = ''
        for index in range ( len(self.tokens)-2, 0, -1): #Make sure vars are correct... -2... 0...
            if self.tokens[index] == '-' and self.tokens[index - 1] == '-':
                # Check for context: number/bracket to the right, operator to the left
                if  ((self.is_operand(self.tokens[index+1]) or self.tokens[index + 1] == '(') and
                        (index - 2 < 0 or self.tokens[index - 2] in operators_dict or self.tokens[index - 2] == '(')):
                    # Remove the two minuses
                    del self.tokens[index]
                    del self.tokens[index - 1]
                    index -= 1
        # print(f" after delete_extra_unary_minuses: {self.tokens}") # For testing


    def join_number_minuses(self):
        """
        Joins number minuses directly to numbers.
        """
        for index in range(1, len(self.tokens)-1, 1):
            if self.tokens[index] == '-' and ((self.tokens[index-1] in operators_dict and self.tokens[index-1] != '-') or (self.tokens[index-1] == '-' and index-2 >= 0 and (self.tokens[index-2].isdigit() or '.' in self.tokens[index-2] or '_' in self.tokens[index-2]))):
                if ('(' in self.tokens[index + 1]):
                    self.minus_brackets_handle(index)
                else:
                    self.tokens[index + 1] = SIGN_NUMBER_MINUS + self.tokens[index+1]
                    del self.tokens[index]
                    index -= 1 # not sure...
        # print(f" after join_number_minuses: {self.tokens}")  # For testing

    def minus_brackets_handle(self, index: int): # Assuming brackets are valid
        """
        :param index: index of minus in self.tokens
        :type index: int
        """
        self.tokens.insert(index, '(')
        # print(f"og: {self.tokens}")
        index+=3
        # print(f"in index: {index} = {self.tokens[index]}")
        track_brackets = ['(']
        while track_brackets:
            # print(f"tracking: {track_brackets}")
            if (self.tokens[index] == '('):
                track_brackets.append('(')
            if (self.tokens[index] == ')'):
                if track_brackets:
                    self.tokens.insert(index, ')')
                    return
                else:
                    track_brackets.pop()
            index+=1

    def replace_unary_minuses(self):
        """
        Replaces all appearances of unary minuses with SIGN_UNARY_MINUS [';']
        """
        for index in range(0, len(self.tokens)-1, 1):
            if self.tokens[index] == '-' and (index == 0 or '(' in self.tokens[index-1] ):
                self.tokens[index] = SIGN_UNARY_MINUS
        # print(f" after replace_unary_minus: {self.tokens}")  # For testing

    def infix_to_postfix(self):
        """
        Converts the tokenized infix equation to a postfix stack.
        """
        stack = []
        postfix = []
        index = 0
        for token in self.tokens:
            if self.is_operand(token) or SIGN_NUMBER_MINUS in token:  # Operand
                postfix.append(token)
            elif token is UnaryOperator:
                if operator_registery.is_left_unary_operator(token):  # Push left-sided unary operator
                    stack.append(token)
                else:  # Right-sided unary operators
                    if index > 0 and self.is_operand(self.tokens[index - 1]):
                        postfix.append(token)
                    else:
                        stack.append(token)
            elif token == '(':
                stack.append(token)
            elif token == ')':
                while stack[-1] != '(' and stack[-1] != SIGN_NUMBER_MINUS+'(':
                    postfix.append(stack.pop())
                if (stack[-1] != SIGN_NUMBER_MINUS+'('):
                    pass # Insert negative value of result in brackets...
                stack.pop()
            else:  # Operator
                while stack and stack[-1] != '(' and self.precedence(token) <= self.precedence(stack[-1]): # add '-('
                    postfix.append(stack.pop())
                stack.append(token)
            index+=1

        while stack:
            postfix.append(stack.pop())

        self.postfix_stack = postfix
        # print(f"Postfix stack: {self.postfix_stack}")  # For testing

    def solve_postfix(self):
        """
        Solves the equation represented by postfix stack and updates the result.
        """
        stack = []
        for token in (self.postfix_stack):
            if self.is_operand(token) or SIGN_NUMBER_MINUS in token:  # Operand
                stack.append(float(token.replace(SIGN_NUMBER_MINUS, '-')))
            else:
                operand1 = stack.pop()
                # Temp implementation.
                # TODO: improve. avoid messy if-elif-else struct.
                if token in unary_operators_dict:
                    unary_result = unary_operators_dict.get(token).solve(operand1)
                    stack.append(unary_result)
                elif token in binary_operators_dict:
                    operand2 = stack.pop()
                    binary_result = binary_operators_dict.get(token).solve(operand2, operand1)
                    stack.append(binary_result)
        self.result = stack[0] if stack  else "Nothing to calculate."