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
        self.remove_unaries() #test
        return self.equation

    def remove_white_spaces(self):
        """
        Removes white spaces from str equation.
        """
        self.equation = self.equation.replace(' ', '')

    def remove_unaries(self): #TODO: implement
        """
        Removes extra unary minuses from str equation.
        """
        pass

    def remove_unaries2(self): # IGNORE - Test func...
        print(f"Before: {self.equation}")
        result = ""
        i = 0
        while i < len(self.equation):
            if i + 1 < len(self.equation) and self.equation[i] == '-' and self.equation[i + 1] == '-':
                char_before = self.equation[i - 1] if i > 0 else None
                char_after = self.equation[i + 2] if i + 2 < len(self.equation) else None

                if char_before and char_before.isdigit():
                    result += '-'
                i += 2
            else:
                result += self.equation[i]
                i += 1

        self.equation = result
        print(f"After: {self.equation}")


    def remove_unaries3(self): # IGNORE - Test 2
        print(f"Before: {self.equation}")
        result = ""
        i = 0
        while i < len(self.equation):
            if i + 1 < len(self.equation) and self.equation[i] == '-' and self.equation[i + 1] == '-':
                char_before = self.equation[i - 1] if i > 0 else None
                char_after = self.equation[i + 2] if i + 2 < len(self.equation) else None
                if char_before and char_before.isdigit():
                    result += '-'
                else:
                    result += '+'
                i += 2
            else:
                result += self.equation[i]
                i += 1

        result = result.replace('+-', '-').replace('-+', '-').replace('++', '+')
        self.equation = result
        print(f"After: {self.equation}")