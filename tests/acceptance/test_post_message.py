from unittest import TestCase
from unittest.mock import Mock, call

from datetime import datetime, timedelta

from social_network.cli import SocialNetworkCLI
from social_network.api import SocialNetworkAPI
from social_network.repo import SocialNetworkRepo
from social_network.util_wrappers import InputWrapper, PrintWrapper
from social_network.clock import Clock
from social_network.formatter import Formatter


class TestSocialNetwork(TestCase):
    def setUp(self):
        self.mock_clock = Mock(Clock)
        self.repo = SocialNetworkRepo(self.mock_clock)
        self.formatter = Formatter()
        self.api = SocialNetworkAPI(self.repo, self.formatter)
        self.mock_input = Mock(InputWrapper)
        self.mock_printer = Mock(PrintWrapper)

        self.cli = SocialNetworkCLI(
            input_wrapper=self.mock_input,
            social_network_api=self.api,
            print_wrapper=self.mock_printer,
        )


    def test_user_can_post_and_read_a_message(self):
        user_input = ["Alice -> I love the weather today", "Alice", "exit"]
        current_time = datetime.now()
        time_difference = current_time - timedelta(minutes=5)
        self.mock_input.read_input.side_effect = user_input
        self.mock_clock.get_current_datetime.side_effect = [
            time_difference,
            current_time,
        ]

        self.cli.start()

        self.mock_printer.output.assert_has_calls([
            call("I love the weather today (5 minutes ago)"),
            call("Toodaloo!")
            ])

    # def test_following_and_wall(self):
    #     user_input = [
    #         "Charlie -> Hellow world",
    #         "Alice -> I love the weather today",
    #         "Charlie wall",
    #         "Charlie follows Alice",
    #         "Charlie wall",
    #         "exit",
    #     ]
    #     current_time = datetime.now()
    #     self.mock_input.read_input.side_effect = user_input
    #     self.mock_clock.get_current_datetime.side_effect = [
    #         current_time - timedelta(minutes=10 - i*2) for i in range(6)
    #     ]

    #     self.cli.start()

    #     self.mock_printer.output.assert_called_with(
    #         "Charlie - Hellow world (4 minutes ago)",
    #         "Charlie - Hellow world (8 minutes ago)\nAlice - I love the weather today (6 minutes ago)"
    #     )
