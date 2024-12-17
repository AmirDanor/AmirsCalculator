# Constants
from calculator.utils.operator_registry import OperatorRegistry # temp implementation. TODO: delete later to avoid high coupling.

operator_registry = OperatorRegistry() #todo: change ??? because its a var in module...

MINUS = '-'

NUMBER_MINUS = '_'

UNARY_MINUS = ';'

ALLOWED_BEFORE_RIGHT_UNARY = ({str(i) for i in range(10)} # int numbers 0 - 9 as str
                                 .union({ ')', '!', '#'}) #TODO: link with actual set. make it more modular
                          )
ALLOWED_AFTER_RIGHT_UNARY = (set(operator_registry.get_right_unary_operators())
                             .union(operator_registry.get_binary_operators())
                             .union({')'}))