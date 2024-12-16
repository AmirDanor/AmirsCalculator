from calculator.utils.operator_registry import OperatorRegistry


# Methods
def is_operand(string: str) -> bool:
    """
    Checks if string is operand
    :param string: string to check
    :type string: str
    :return: True if string is operand, else return False
    :rtype: bool
    """
    return string.isdigit() or '.' in string or '_' in string

def precedence(operator):
    """
    Gets operand's precedence
    :param operator: representation of operator
    :type operator: str
    :return: operator's precedence
    :rtype: int
    """
    return OperatorRegistry().get_precedence_for_operator(operator) # temp implementation. TODO: delete later to avoid high coupling.