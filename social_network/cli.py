from social_network.api import SocialNetworkAPI
from social_network.util_wrappers import InputWrapper, PrintWrapper
from social_network.parse_input import ParseInput


class SocialNetworkCLI:

    def __init__(
        self,
        input_wrapper: InputWrapper,
        print_wrapper: PrintWrapper,
        social_network_api: SocialNetworkAPI,
    ):
        self.input_wrapper = input_wrapper
        self.parse_input = ParseInput(social_network_api)

    def start(self):
        print("Welcome to the Social Network CLI")
        print("Type 'help' for a list of commands")

        while True:
            command = self.input_wrapper.read_input()
            self.parse_input.process(command)

            if command == "exit":
                print("Toodaloo!")
                break
