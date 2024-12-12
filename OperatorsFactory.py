from Operators import Add, Sub, Mul, Div, Pow, Mod, Max, Min, Avg, Neg, Fac, Sum

class OperatorFactory:
    """
    A factory for mapping operator functions by string representation (Using Dictionaries).
    Separate dictionaries for unary / binary operators.
    """

    def __init__(self):
        """Initialize the operator dictionaries (separated by unary / binary) with default binary and unary operators."""
        self._unary_operators_funcs = {
            '~': Neg(),
            '!': Fac(),
            '#': Sum()
        }
        self._binary_operators_funcs = {
            '+': Add(),
            '-': Sub(),
            '*': Mul(),
            '/': Div(),
            '^': Pow(),
            '%': Mod(),
            '$': Max(),
            '&': Min(),
            '@': Avg()
        }

    def get_all_operator_symbols(self):
        """
        :return: all operator symbols
        :rtype: set
        """
        return (set(self._unary_operators_funcs.keys())
                .union(self._binary_operators_funcs.keys()))

    def get_unary_operators(self):
        return self._unary_operators_funcs

    def get_binary_operators(self):
        return self._binary_operators_funcs

    def get_precedence(self, operator):
        """
        :param operator: a valid operator
        :type operator: str
        :return: precedence of operator
        :rtype:
        """
        if operator in self._unary_operators_funcs:
            return self._unary_operators_funcs.get(operator).get_precedence()
        elif operator in self._binary_operators_funcs:
            return self._binary_operators_funcs.get(operator).get_precedence()
        return None