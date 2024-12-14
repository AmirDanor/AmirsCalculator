VALID_INPUT_CHARACTERS = ({str(i) for i in range(10)}
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