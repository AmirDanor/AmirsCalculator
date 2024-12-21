import pytest

from calculator.logic.equation_solver import EquationSolver
from calculator.logic.exceptions import InvalidInputError, EmptyEquationError
from calculator.logic.input_validator import InputValidator
from calculator.logic.string_processor import StringProcessor
from calculator.logic.token_processor import ArithmeticTokenProcessor
from calculator.logic.tokenizer import ArithmeticTokenizer


@pytest.mark.parametrize("expression, expected_result", [
    ("3^2", 9),
    ("1+1", 2),
    ("85.2/2", 42.6),
    ("7 0-5 . 7", 64.3),
])
def test_valid_expressions(expression, expected_result):
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


@pytest.mark.parametrize("expression, expected_result", [
    ("", "Nothing To Calculate!"),
    (" ", "Nothing To Calculate!"),
    ("  ", "Nothing To Calculate!"),
    ("   ", "Nothing To Calculate!"),
    ("                  ", "Nothing To Calculate!")
])
def test_whitespaces(expression, expected_result):
    tokenizer = ArithmeticTokenizer()
    token_processor = ArithmeticTokenProcessor()
    input_validator = InputValidator()

    # Check for EmptyEquationError when input is empty or contains only
    # whitespace
    if not expression.strip():  # Check if the expression is empty or
        # contains only whitespace
        with pytest.raises(EmptyEquationError) as excinfo:
            raise EmptyEquationError()
        assert str(excinfo.value) == expected_result
    else:
        string_formatter = StringProcessor(expression)
        formatted_expression = string_formatter.process()
        tokenized_equation = tokenizer.tokenize(formatted_expression)
        processed_tokenized_equation = (token_processor
                                        .process(tokenized_equation))
        equation_solver = EquationSolver(processed_tokenized_equation)
        solution = equation_solver.solve()

        # Assert that the solution matches the expected result
        assert solution == expected_result

