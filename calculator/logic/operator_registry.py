from calculator.logic.operators import Add, Sub, Mul, Div, UMin, Pow, Mod, Max, Min, Avg, Neg, Fac, Sum


class OperatorRegistry:
    """
    A registry for mapping operator functions by string representation (Using Dictionaries).
    Separate dictionaries for unary / binary operators.
    """

    def __init__(self):
        """Initialize the operator dictionaries (separated by unary / binary) with default binary and unary operators."""
        self._unary_operators_funcs = {
            ';': UMin(),
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
        Get all operators str symbol representation as set

        :return: all operator symbols
        :rtype: set
        """
        return (set(self._unary_operators_funcs.keys())
                .union(self._binary_operators_funcs.keys()))

    def get_unary_operators(self):
        """
        Get all unary operators str symbol representation as set

        :return: all unary operator symbols
        :rtype: set
        """
        return self._unary_operators_funcs

    def get_binary_operators(self):
        """
        Get all binary operators str symbol representation as set

        :return: all binary operator symbols
        :rtype: set
        """
        return self._binary_operators_funcs

    def get_precedence_for_operator(self, operator):
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

    def is_left_unary_operator(self, operator: str):
        """
        Check if the given operator is a left unary operator.

        :param operator: a mathematical operator
        :type operator: str
        :return: True if operator is a left unary operator, False if operator is a right unary operator. otherwise: None
        :rtype: Any
        """
        if operator in self._unary_operators_funcs:
            return self._unary_operators_funcs.get(operator).is_left()
        return None