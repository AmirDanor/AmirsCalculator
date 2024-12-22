"""
General utils module which contains general constants used
across the calculator.
"""

# Constants

QUIT_STR = 'quit'  # string which user has to enter to end program.

OPEN_BRACKETS = '('

CLOSE_BRACKETS = ')'

DOT = '.'

EMPTY_STR = ''

EMPTY_CHARACTERS = {
    ' ',
    '\t'
}

VALID_INPUT_CHARACTERS = (
    {str(i) for i in range(10)}  # int numbers 0 - 9 as str
    .union({'+',
            '-',
            '*',
            '/',
            '^',
            '%',
            '$',
            '&',
            '@',
            '~',
            '!',
            '#',
            '(',
            ')',
            '.',
            ' ',
            '\t'})
)
