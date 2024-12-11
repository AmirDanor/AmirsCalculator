# File contains prints for dev tests

operator_strength = { # TODO: avoid dup with InputValidator.py
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2,
    '^': 3,
    '%': 4,
    '$': 5,
    '&': 5,
    '@': 5,
    '~': 6,
    '!': 6
}

class EquationSolver:
    def __init__(self, equation: str):
        """
        Solves the equation.

        :param equation: User's input.
        :type equation: str
        """
        self.equation = equation
        self.tokens = []
        self.prefix_stack = []
        self.result = None

    def solve(self):
        """
        Solves the equation by calling the class' functions.

        :return: Solution to equation
        :rtype: float
        """
        self.tokenize()
        self.infix_to_postfix()
        self.solve_postfix()
        return self.result

    def tokenize(self):
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
                if character in operator_strength or character in '()':
                    tokens.append(character)
        if number != '':
            tokens.append(number)
        self.tokens = tokens
        print(self.tokens)

    def strength(self, op):
        return operator_strength.get(op, -1)

    def infix_to_postfix(self):
        """
        Converts the tokenized infix equation to a postfix stack.
        """
        stack = []
        postfix = []

        for token in self.tokens:
            if token.isdigit() or '.' in token:  # Operand
                postfix.append(token)
            elif token == '(':
                stack.append(token)
            elif token == ')':
                while stack[-1] != '(':
                    postfix.append(stack.pop())
                stack.pop()
            else:  # Operator
                while stack and self.strength(token) <= self.strength(stack[-1]):
                    postfix.append(stack.pop())
                stack.append(token)

        while stack:
            postfix.append(stack.pop())

        self.prefix_stack = postfix
        print(f"Prefix stack: {self.prefix_stack}")  # For testing

    def solve_postfix(self):
        """
        Solves the equation represented by postfix stack and updates the result.
        """

        stack = []
        for token in (self.prefix_stack):
            if token.isdigit() or '.' in token:  # Operand
                stack.append(float(token))
            else:
                b = stack.pop()
                a = stack.pop()
                # Temp implementation.
                # TODO: improve. avoid messy if-elif-else struct.
                if token == '+':
                    stack.append(a + b)
                elif token == '-':
                    stack.append(a - b)
                elif token == '*':
                    stack.append(a * b)
                elif token == '/':
                    stack.append(a / b)
                elif token == '^':
                    stack.append(a ** b)
                elif token == '%':
                    stack.append(a % b)
                elif token == '$':
                    stack.append(max(a, b))
                elif token == '&':
                    stack.append(min(a, b))
                elif token == '@':
                    stack.append((a + b)/2)
        self.result = stack[0] if stack else None