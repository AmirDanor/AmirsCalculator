OPEN_BRACKETS = '('

CLOSE_BRACKETS = ')'

EMPTY_CHARACTERS = {
    ' ',
    '\t'
}

VALID_INPUT_CHARACTERS = ({str(i) for i in range(10)} # int numbers 0 - 9 as str
                                 .union({ '+',
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