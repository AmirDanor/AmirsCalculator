from InputHandler import InputHandler


class ConsoleInputHandler(InputHandler):
    """
    Class responsible for getting an input from user through console.
    """
    def get_input(self):
        """
        Get input from user through console
        :return: user input
        """
        return input()