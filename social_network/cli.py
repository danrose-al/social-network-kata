from social_network.api import SocialNetworkAPI
from social_network.util_wrappers import InputWrapper, PrintWrapper
from social_network.parse_input import ParseInput


class SocialNetworkCLI:

    def __init__(
        self,
        input_wrapper: InputWrapper = None,
        print_wrapper: PrintWrapper = None,
        social_network_api: SocialNetworkAPI = SocialNetworkAPI(),
    ):
        self.input_wrapper = input_wrapper or InputWrapper()
        self.parse_input = ParseInput()

    def start(self):
        # raise NotImplementedError
        print("Welcome to the Social Network CLI")
        print("Type 'help' for a list of commands")

        while True:
            command = self.input_wrapper.read_input()
            
            if command == "exit":
                print("Toodaloo!")
                break

