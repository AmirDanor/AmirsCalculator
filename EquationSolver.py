# File contains prints for dev tests
from Operators import UnaryOperator
from OperatorsFactory import OperatorFactory

SIGN_NUMBER_MINUS = '_'
SIGN_UNARY_MINUS = ';'

operator_factory = OperatorFactory()
unary_operators_dict = operator_factory.get_unary_operators()
binary_operators_dict = operator_factory.get_binary_operators()
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
        return self.result

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
                if  ((self.tokens[index + 1].isdigit() or self.tokens[index + 1] == '(') and
                        (index - 2 < 0 or self.tokens[index - 2] in operators_dict)):
                    # Remove the two minuses
                    del self.tokens[index]
                    del self.tokens[index - 1]
                    index -= 1
        # print(f" after delete_extra_unary_minuses: {self.tokens}") # For testing


    def join_number_minuses(self):
        """
        Joins number minuses directly to numbers.
        """
        for index in range(2, len(self.tokens)-1, 1):
            if self.tokens[index] == '-' and ((self.tokens[index-1] in operators_dict and self.tokens[index-1] != '-') or (self.tokens[index-1] == '-' and index-2 >= 0 and (self.tokens[index-2].isdigit() or '.' in self.tokens[index-2] or '_' in self.tokens[index-2]))):
                self.tokens[index + 1] = SIGN_NUMBER_MINUS + self.tokens[index+1]
                del self.tokens[index]
                index -= 1 # not sure...
        # print(f" after join_number_minuses: {self.tokens}")  # For testing

    def replace_unary_minuses(self):
        """
        Replaces all appearances of unary minuses with SIGN_UNARY_MINUS [';']
        """
        for index in range(0, len(self.tokens)-1, 1):
            if self.tokens[index] == '-' and index == 0 or self.tokens[index-1] == '(':
                self.tokens[index] = SIGN_UNARY_MINUS
        # print(f" after replace_unary_minus: {self.tokens}")  # For testing

    def precedence(self, operator):
        """
        :param operator: representation of operator
        :type operator: str
        :return: operator's precedence
        :rtype: int
        """
        return operator_factory.get_precedence(operator)

    def infix_to_postfix(self):
        """
        Converts the tokenized infix equation to a postfix stack.
        """
        stack = []
        postfix = []
        index = 0
        for token in self.tokens:
            if token.isdigit() or '.' in token or SIGN_NUMBER_MINUS in token:  # Operand
                postfix.append(token)
            elif token is UnaryOperator:
                if operator_factory.is_left_unary_operator(token):  # Push left-sided unary operator
                    stack.append(token)
                else:  # Right-sided unary operators
                    if index > 0 and (self.tokens[index - 1].isdigit() or '.' in self.tokens[index - 1]):
                        postfix.append(token)
                    else:
                        stack.append(token)
            elif token == '(':
                stack.append(token)
            elif token == ')':
                while stack[-1] != '(': # add '-('
                    postfix.append(stack.pop())
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
            if token.isdigit() or '.' in token or SIGN_NUMBER_MINUS in token:  # Operand
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
        self.result = stack[0] if stack else "Nothing to calculate."