from social_network.api import SocialNetworkAPI
from social_network.util_wrappers import InputWrapper, PrintWrapper
from social_network.parse_input import ParseInput


class SocialNetworkCLI:
    """
    SocialNetworkCLI class is responsible for handling user input and output
    """

    def __init__(
        self,
        input_wrapper: InputWrapper,
        print_wrapper: PrintWrapper,
        social_network_api: SocialNetworkAPI,
    ):
        self.input_wrapper = input_wrapper
        self.parse_input = ParseInput(social_network_api)
        self.print_wrapper = print_wrapper

    def start(self):
        self.print_wrapper.output("Welcome to the Social Network CLI")
        self.print_wrapper.output("Type 'help' for a list of commands")

        while True:
            command = self.input_wrapper.read_input()
            output = self.parse_input.process(command)

            if output:
                self.print_wrapper.output(output)

            if command == "exit":
                self.print_wrapper.output("Toodaloo!")
                break
