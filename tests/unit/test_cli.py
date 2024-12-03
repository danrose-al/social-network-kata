from unittest import TestCase
from unittest.mock import Mock
from social_network.cli import SocialNetworkCLI
from social_network.api import SocialNetworkAPI
from social_network.util_wrappers import InputWrapper
from social_network.util_wrappers import PrintWrapper
from social_network.parse_input import ParseInput


class TestSocialNetworkCLI(TestCase):

    def test_cli_gets_input(self):
        input_wrapper = Mock(InputWrapper)
        print_wrapper = Mock(PrintWrapper)
        social_network_api = Mock(SocialNetworkAPI)
        social_network_cli = SocialNetworkCLI(
            input_wrapper, print_wrapper, social_network_api
        )
        input_wrapper.read_input.side_effect = [
            "Alice -> I love the weather today",
            "exit",
        ]

        social_network_cli.start()

        self.assertEqual(input_wrapper.read_input.call_count, 2)

    def test_cli_parses_input(self):
        input_wrapper = Mock(InputWrapper)
        print_wrapper = Mock(PrintWrapper)
        social_network_api = Mock(SocialNetworkAPI)
        parse_input = Mock(ParseInput)
        social_network_cli = SocialNetworkCLI(
            input_wrapper, print_wrapper, social_network_api
        )
        social_network_cli.parse_input = parse_input
        input_wrapper.read_input.side_effect = [
            "Alice -> I love the weather today",
            "exit",
        ]

        social_network_cli.start()

        social_network_cli.parse_input.process.assert_called()
