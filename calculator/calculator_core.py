"""
Module contains CalculatorCore class which ensures correct calcultor workflow.
"""

from calculator.interaction import input_handler, message_handler

from calculator.logic.equation_solver import EquationSolver
from calculator.logic.exceptions import EmptyParenthesesError, UnaryError, \
    NegativeFactorialError, LargeFactorialError, \
    NegativeSumError, LargeSumError, InvalidInputError, \
    UnmatchedOpeningParenthesesError, NonIntFactorialError, \
    UnmatchedClosingParenthesesError, NegativeRootError, ZeroBaseNegExError, \
    MultipleDotsError, \
    MultipleDotsOperandError, SingleDotError, DivisionByZeroError, \
    OperatorUsageError, ModuloByZeroError, EmptyEquationError, \
    WrongParenthesesUsageError, ExpectedOperandError
from calculator.logic.string_processor import StringProcessor
from calculator.logic.token_processor import TokenProcessor
from calculator.logic.string_preprocessor import StringPreprocessor
from calculator.logic.tokenizer import Tokenizer

QUIT_STR = 'quit'  # string which user has to enter to end program.


class CalculatorCore:
    """
    Class responsible for calling other functions from other classes.
    Contains core logic for handling the calculator workflow.
    """

    def __init__(self, message_handler: message_handler.MessageHandler,
                 input_handler: input_handler.InputHandler,
                 string_preprocessor: StringPreprocessor,
                 string_processor: StringProcessor,
                 tokenizer: Tokenizer, token_processor: TokenProcessor):
        """
        Initializes the calculator core with required components.

        :param message_handler: An instance of the MessageHandler class
            to display prompts and messages.
        :type message_handler: MessageHandler
        :param input_handler: An instance of the InputHandler class
            to get user input.
        :type input_handler: InputHandler
        :param string_preprocessor: An instance of the StringPreprocessor class
            to preprocess user's input
        :type string_preprocessor: StringPreprocessor
        :param string_processor: An instance of the StringProcessor class
            to process user's input
        :type string_processor: StringProcessor
        :param tokenizer: An instance of the Tokenizer class to tokenize
            user's input
        :type tokenizer: Tokenizer
        :param token_processor: An instance of the TokenProcessor class
            to process tokenized user's input
        :type token_processor: TokenProcessor
        """

        self.message_handler = message_handler
        self.input_handler = input_handler
        self.string_preprocessor = string_preprocessor
        self.string_processor = string_processor
        self.tokenizer = tokenizer
        self.token_processor = token_processor

    def run(self):
        """
        Runs the program as intended, in correct order.
        """
        self.message_handler.display_input_message()
        try:
            expression = self.get_input_loop()
            while expression != QUIT_STR:
                try:
                    self.string_preprocessor.preprocess(expression)
                    expression = self.string_processor.process(expression)
                    tokenized_equation = self.tokenizer.tokenize(
                        expression)
                    processed_tokenized_equation = (
                        self.token_processor.process(tokenized_equation))
                    equation_solver = EquationSolver(
                        processed_tokenized_equation)
                    solution = equation_solver.solve()
                    if solution is not None:
                        self.message_handler.display_result_message(
                            str(solution))
                except InvalidInputError as iie:
                    self.handle_display_error(iie)
                except EmptyEquationError as eee:
                    self.handle_display_error(eee)
                except NonIntFactorialError as nife:
                    self.handle_display_error(nife)
                except UnmatchedOpeningParenthesesError as uope:
                    self.handle_display_error(uope)
                except UnmatchedClosingParenthesesError as ucpe:
                    self.handle_display_error(ucpe)
                except WrongParenthesesUsageError as wpue:
                    self.handle_display_error(wpue)
                except EmptyParenthesesError as epe:
                    self.handle_display_error(epe)
                except SingleDotError as sde:
                    self.handle_display_error(sde)
                except MultipleDotsError as mde:
                    self.handle_display_error(mde)
                except MultipleDotsOperandError as mdoe:
                    self.handle_display_error(mdoe)
                except UnaryError as ue:
                    self.handle_display_error(ue)
                except DivisionByZeroError as dbze:
                    self.handle_display_error(dbze)
                except ModuloByZeroError as mbze:
                    self.handle_display_error(mbze)
                except ZeroBaseNegExError as zbnee:
                    self.handle_display_error(zbnee)
                except NegativeRootError as nre:
                    self.handle_display_error(nre)
                except NegativeFactorialError as nfe:
                    self.handle_display_error(nfe)
                except LargeFactorialError as lfe:
                    self.handle_display_error(lfe)
                except NegativeSumError as nse:
                    self.handle_display_error(nse)
                except LargeSumError as lse:
                    self.handle_display_error(lse)
                except OperatorUsageError as oue:
                    self.handle_display_error(oue)
                except ExpectedOperandError as eoe:
                    self.handle_display_error(eoe)
                except IndexError as ie:
                    self.handle_display_error(ie)
                except OverflowError as oe:
                    # oe.args[-1] = error message
                    if oe.args[-1] == 'math range error':
                        self.handle_display_error(f"Error! result is out of "
                                                  f"calculator's range")
                    else:
                        self.handle_display_error(f"Error! {oe.args[-1]}")
                except Exception as e:
                    self.handle_display_error(e)

                self.message_handler.display_input_message()
                expression = self.get_input_loop()

        except KeyboardInterrupt:
            self.handle_display_error(f"\nKeyboard Interrupt detected. ")

        self.message_handler.display_quit_message()

    def handle_display_error(self, error):
        """
        Helper method to display error messages.

        :param error: Error which should be displayed to user.
        :type error: str or Exception
        """

        self.message_handler.display_error_message(str(error))

    def get_input_loop(self):
        """
        Ensures correct input-looping without crashing because of EOFError.

        :return: User's input
        :rtype: str
        """

        while True:
            try:
                expression = self.input_handler.get_input()

                return expression

            except EOFError:
                self.handle_display_error(
                    f"EOF detected. If you'd like to stop "
                    f"program, please enter '{QUIT_STR}'.")
                self.message_handler.display_input_message()
