import pytest

from calculator.logic.equation_solver import EquationSolver
from calculator.logic.exceptions import InvalidInputError, \
    EmptyEquationError, OperatorUsageError, MultipleDotsOperandError, \
    UnmatchedOpeningParenthesesError, EmptyParenthesesError, UnaryError
from calculator.logic.string_preprocessor import StringPreprocessor
from calculator.logic.string_processor import StringProcessor
from calculator.logic.token_processor import ArithmeticTokenProcessor
from calculator.logic.tokenizer import ArithmeticTokenizer


# Syntax errors
@pytest.mark.parametrize("expression, expected_exception", [
    ("3^*2", OperatorUsageError),
    ("8.6..30+10", MultipleDotsOperandError),
    ("5+(10", UnmatchedOpeningParenthesesError),
    ("20.8^()+4", EmptyParenthesesError),
    ("123!+#678", UnaryError)
])
def test_syntax_errors(expression, expected_exception):
    with pytest.raises(expected_exception):
        string_preprocessor = StringPreprocessor(expression)
        string_preprocessor.preprocess()
        string_processor = StringProcessor(expression)
        expression = string_processor.process()
        tokenizer = ArithmeticTokenizer()
        token_processor = ArithmeticTokenProcessor()
        string_formatter = StringProcessor(expression)
        formatted_expression = string_formatter.process()
        tokenized_equation = tokenizer.tokenize(formatted_expression)
        processed_tokenized_equation = token_processor.process(
            tokenized_equation)
        equation_solver = EquationSolver(processed_tokenized_equation)
        equation_solver.solve()


# Gibberish
@pytest.mark.parametrize("expression", [
    "qqquittt!!!!",
    "Om-eG+A",
    "123ma_kore0 hjiopo 3koi3pjyg",
    "htrh645 4w",
])
def test_gibberish(expression):
    # Expecting InvalidInputError to be raised
    with pytest.raises(InvalidInputError):
        string_preprocessor = StringPreprocessor(expression)
        string_preprocessor.preprocess()  # Expected to raise InvalidInputError
        string_processor = StringProcessor(expression)
        expression = string_processor.process()
        tokenizer = ArithmeticTokenizer()
        token_processor = ArithmeticTokenProcessor()
        string_formatter = StringProcessor(expression)
        formatted_expression = string_formatter.process()
        tokenized_equation = tokenizer.tokenize(formatted_expression)
        processed_tokenized_equation = token_processor.process(
            tokenized_equation)
        equation_solver = EquationSolver(processed_tokenized_equation)
        equation_solver.solve()


# Empty str + Whitespaces
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

    with pytest.raises(EmptyEquationError):
        string_preprocessor = StringPreprocessor(expression)
        string_preprocessor.preprocess()  # Expected to raise EmptyEquationError
        string_processor = StringProcessor(expression)
        expression = string_processor.process()
        tokenizer = ArithmeticTokenizer()
        token_processor = ArithmeticTokenProcessor()
        string_formatter = StringProcessor(expression)
        formatted_expression = string_formatter.process()
        tokenized_equation = tokenizer.tokenize(formatted_expression)
        processed_tokenized_equation = token_processor.process(
            tokenized_equation)
        equation_solver = EquationSolver(processed_tokenized_equation)
        equation_solver.solve()


# 15 simple valid equations
@pytest.mark.parametrize("expression, expected_result", [
    ("30.1+4.43", 34.53),
    ("12-30.4", -18.4),
    ("2.2*-4", -8.8),
    ("2.2/-16", -0.1375),
    ("-2.2/-16", 0.1375),
    ("3^2", 9),
    ("4^-2", 0.0625),
    ("13%-4", -3),
    ("12$-6.8", 12),
    ("12&-6.8", -6.8),
    ("12@-6.8", 2.6),
    ("~12.4", -12.4),
    ("6!", 720),
    ("123.45#", 15),
    ("-123.4#", -10)
])
def test_simple_valid_expressions(expression, expected_result):
    tokenizer = ArithmeticTokenizer()
    token_processor = ArithmeticTokenProcessor()

    string_formatter = StringProcessor(expression)
    formatted_expression = string_formatter.process()
    tokenized_equation = tokenizer.tokenize(formatted_expression)
    processed_tokenized_equation = token_processor.process(tokenized_equation)
    equation_solver = EquationSolver(processed_tokenized_equation)
    solution = equation_solver.solve()

    assert solution == expected_result


# 20 complex valid equations
@pytest.mark.parametrize("expression, expected_result", [
    ("007^(2+--3!)#*123-99.5", 709070423.5),
    ("(20%(12+54#!$(43@771&99)))", 20),
    ("-1234.5678987654321#^3", -531441),
    ("~--(3+7)+1234#@(12*4)^2", 831),
    ("(1 + 2) * 2$ 12.34#-90.51+~17", -77.51),
    ("98+--2!^(--1@123)&-(12#)", 98.125),
    ("(1+2-3*4/2^2)&(-1234567890#)", -45),
    # TODO: add more tests
])
def test_simple_valid_expressions(expression, expected_result):
    tokenizer = ArithmeticTokenizer()
    token_processor = ArithmeticTokenProcessor()

    string_formatter = StringProcessor(expression)
    formatted_expression = string_formatter.process()
    tokenized_equation = tokenizer.tokenize(formatted_expression)
    processed_tokenized_equation = token_processor.process(tokenized_equation)
    equation_solver = EquationSolver(processed_tokenized_equation)
    solution = equation_solver.solve()

    assert solution == expected_result
