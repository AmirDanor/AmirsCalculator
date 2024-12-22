"""
Operator utils module which contains operator-related constants used across the
calculator.
"""
# Constants

SIGN_MINUS_SYMBOL = '_'

ADD_SYMBOL = '+'
SUB_SYMBOL = '-'
MUL_SYMBOL = '*'
DIV_SYMBOL = '/'
POW_SYMBOL = '^'
MOD_SYMBOL = '%'
MAX_SYMBOL = '$'
MIN_SYMBOL = '&'
AVG_SYMBOL = '@'
UNARY_MINUS_SYMBOL = ';'
NEG_SYMBOL = '~'
FAC_SYMBOL = '!'
SUM_SYMBOL = '#'

# Sets of operators by type
LEFT_UNARY_OPERATORS = {UNARY_MINUS_SYMBOL, NEG_SYMBOL}
RIGHT_UNARY_OPERATORS = {FAC_SYMBOL, SUM_SYMBOL}
BINARY_OPERATORS = {ADD_SYMBOL, SUB_SYMBOL, MUL_SYMBOL, DIV_SYMBOL, POW_SYMBOL,
                    MOD_SYMBOL, MAX_SYMBOL, MIN_SYMBOL, AVG_SYMBOL}
ALL_UNARY_OPERATORS = LEFT_UNARY_OPERATORS | RIGHT_UNARY_OPERATORS
ALL_OPERATORS = ALL_UNARY_OPERATORS | BINARY_OPERATORS


ALLOWED_BEFORE_RIGHT_UNARY = (
    {str(i) for i in range(10)}  # int numbers 0 - 9 as str
    .union({')', '!', '#'})
)

ALLOWED_AFTER_RIGHT_UNARY = (RIGHT_UNARY_OPERATORS.union(BINARY_OPERATORS)
                             .union({')'}))
