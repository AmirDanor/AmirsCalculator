from calculator.utils import general_utils


class StringProcessor:
    def __init__(self, equation: str):
        """
        Process (reformat) users' input.

        :param equation: User's input (equation)
        :type equation: str
        """
        self._equation = equation

    def process(self):
        """
        Process (fix format) of user's input.

        :return: Processed user's input (equation with fixed format)
        :rtype: str
        """
        self.remove_white_spaces()
        return self._equation

    def remove_white_spaces(self):
        """
        Removes white spaces from str equation.
        """
        self._equation = ''.join(c for c in self._equation if
                                 c not in general_utils.EMPTY_CHARACTERS)
