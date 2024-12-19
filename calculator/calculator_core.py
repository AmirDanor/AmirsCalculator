# File contains prints for dev tests

from calculator.interaction import input_handler, message_handler
from calculator.logic import input_validator

from calculator.logic.equation_solver import EquationSolver
from calculator.logic.exceptions import EmptyParenthesesError, UnaryError, \
    NegativeFactorialError, LargeFactorialError, \
    NegativeSumError, LargeSumError, InvalidInputError, \
    UnmatchedOpeningParenthesesError, NonIntFactorialError, \
    UnmatchedClosingParenthesesError, NegativeRootError, ZeroBaseNegExError, \
    MultipleDotsError, \
    MultipleDotsOperandError, SingleDotError
from calculator.logic.string_preprocessor import StringPreprocessor
from calculator.logic.string_processor import StringProcessor
from calculator.logic.token_processor import TokenProcessor
from calculator.logic.tokenizer import Tokenizer

QUIT_STR = 'quit'  # string which user has to enter to end program.
QUIT_MSG = 'Program Ended.'  # string which get displayed to user after program ends.


class CalculatorCore:
    """
    Class responsible for calling other functions from other classes.
    """

    def __init__(self, message_handler: message_handler.MessageHandler,
                 input_handler: input_handler.InputHandler,
                 tokenizer: Tokenizer, token_processor: TokenProcessor):
        """
        :param message_handler: An instance of the MessageHandler class to display prompts and messages
        :type message_handler: message_handler
        :param input_handler: An instance of the InputHandler class to get user input
        :type input_handler: input_handler
        """
        self.message_handler = message_handler
        self.input_handler = input_handler
        self.input_validator = input_validator.InputValidator()
        self.tokenizer = tokenizer
        self.token_processor = token_processor

    def run(self):
        """
        Runs the program as intended.
        :raises InvalidInputError: If user's input contains forbidden chars.
        """
        self.message_handler.display_input_message()
        try:
            expression = self.input_handler.get_input()
            while expression != QUIT_STR:
                try:
                    if not self.input_validator.validate_input(expression):
                        raise InvalidInputError(expression)
                except InvalidInputError as iie:
                    self.message_handler.display_custom_message(
                        str(iie))  # Catch and print the InvalidInput exception
                else:
                    try:
                        string_preprocessor = StringPreprocessor(expression)
                        string_preprocessor.preprocess()
                        string_processor = StringProcessor(expression)
                        expression = string_processor.process()
                        tokenized_equation = self.tokenizer.tokenize(
                            expression)
                        processed_tokenized_equation = self.token_processor.process(
                            tokenized_equation)
                        # print(self.token_processor.validate())
                        equation_solver = EquationSolver(
                            processed_tokenized_equation)
                        solution = equation_solver.solve()
                        if solution is not None:  # if solution is not None
                            self.message_handler.display_custom_message(
                                str(solution))
                    except NonIntFactorialError as nife:
                        self.message_handler.display_error_message(
                            nife.__str__())
                    except UnmatchedOpeningParenthesesError as uope:
                        self.message_handler.display_error_message(
                            uope.__str__())
                    except UnmatchedClosingParenthesesError as ucpe:
                        self.message_handler.display_error_message(
                            ucpe.__str__())
                    except EmptyParenthesesError as epe:
                        self.message_handler.display_error_message(
                            epe.__str__())  # TODO: change text displayed
                    except SingleDotError as sde:
                        self.message_handler.display_error_message(
                            sde.__str__())
                    except MultipleDotsError as mde:
                        self.message_handler.display_error_message(
                            mde.__str__())
                    except MultipleDotsOperandError as mdoe:
                        self.message_handler.display_error_message(
                            mdoe.__str__())
                    except UnaryError as ue:
                        self.message_handler.display_error_message(
                            ue.__str__())  # TODO: change text displayed
                    except ZeroDivisionError as zde:
                        self.message_handler.display_error_message(
                            zde.__str__())
                    except ZeroBaseNegExError as zbnee:
                        self.message_handler.display_error_message(
                            zbnee.__str__())
                    except NegativeRootError as nre:
                        self.message_handler.display_error_message(
                            nre.__str__())
                    except NegativeFactorialError as nfe:
                        self.message_handler.display_error_message(
                            nfe.__str__())
                    except LargeFactorialError as lfe:
                        self.message_handler.display_error_message(
                            lfe.__str__())
                    except NegativeSumError as nse:
                        self.message_handler.display_error_message(
                            nse.__str__())
                    except LargeSumError as lse:
                        self.message_handler.display_error_message(
                            lse.__str__())
                    except IndexError as ie:
                        self.message_handler.display_error_message(
                            ie.__str__())  # TODO: change text displayed
                        # triggered by 6-
                        # triggered by (((6)
                    except OverflowError as oe:
                        self.message_handler.display_error_message(
                            f"Error! {oe.args[-1]}")  # oe.args[-1] = error message
                self.message_handler.display_input_message()
                expression = self.input_handler.get_input()
            self.message_handler.display_error_message(QUIT_MSG)
        except KeyboardInterrupt as kie:
            self.message_handler.display_error_message("\nProgram Ended")
