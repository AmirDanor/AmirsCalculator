import pytest

from calculator.logic.equation_solver import EquationSolver
from calculator.logic.exceptions import InvalidInputError
from calculator.logic.input_validator import InputValidator
from calculator.logic.string_processor import StringProcessor
from calculator.logic.token_processor import ArithmeticTokenProcessor
from calculator.logic.tokenizer import ArithmeticTokenizer


@pytest.mark.parametrize("expression, expected_result", [
    "",      # Empty string
    "   ",   # Whitespaces
    "\t\t",  # Tabs

])
def test_multiple_expressions(expression, expected_result):
    tokenizer = ArithmeticTokenizer()
    token_processor = ArithmeticTokenProcessor()
    input_validator = InputValidator()

    # Validate and process the input
    if not input_validator.validate_input(expression):
        raise InvalidInputError(expression)

    string_formatter = StringProcessor(expression)
    formatted_expression = string_formatter.process()
    tokenized_equation = tokenizer.tokenize(formatted_expression)
    processed_tokenized_equation = token_processor.process(tokenized_equation)
    equation_solver = EquationSolver(processed_tokenized_equation)
    solution = equation_solver.solve()

    assert solution == expected_result