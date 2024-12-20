
# Constants

MINUS = '-'

NUMBER_MINUS = '_'

UNARY_MINUS = ';'

POWER = '^'

ALLOWED_BEFORE_RIGHT_UNARY = (
    {str(i) for i in range(10)}  # int numbers 0 - 9 as str
    .union({')', '!', '#'})
    # TODO: link with actual set. make it more modular
)
ALLOWED_AFTER_RIGHT_UNARY = {'#', '!', '+', '-', '*', '/', '%', '^', '$', '@',
                             ')'}
