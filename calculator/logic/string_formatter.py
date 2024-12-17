from calculator.utils import general_utils


class StringFormatter:
    def __init__(self, equation: str):
        """
        Reformats users' input.

        :param equation: User's input (equation)
        :type equation: str
        """
        self.equation = equation


    def fix_format(self):
        """
        Fixes format of user's input.

        :return: User's input (equation) with fixed format
        :rtype: str
        """
        self.remove_white_spaces()
        return self.equation

    def remove_white_spaces(self):
        """
        Removes white spaces from str equation.
        """
        self.equation = ''.join(c for c in self.equation if c not in general_utils.EMPTY_CHARACTERS)