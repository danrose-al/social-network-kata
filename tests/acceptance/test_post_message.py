from unittest import TestCase
from unittest.mock import Mock

from datetime import datetime, timedelta

from social_network.cli import SocialNetworkCLI
from social_network.api import SocialNetworkAPI
from social_network.repo import SocialNetworkRepo
from social_network.util_wrappers import InputWrapper, PrintWrapper
from social_network.clock import Clock


class TestPostMessage(TestCase):

    def test_user_can_post_and_read_a_message(self):
        # ? Objects - User, Post, Wall (API probably cares about these?)
        mock_clock = Mock(Clock)
        mock_repo = Mock(SocialNetworkRepo)
        mock_repo.clock = mock_clock
        social_network_api = SocialNetworkAPI(mock_repo)
        mock_input = Mock(InputWrapper)
        mock_printer = Mock(PrintWrapper)
        cli = SocialNetworkCLI(
            input_wrapper=mock_input,
            social_network_api=social_network_api,
            print_wrapper=mock_printer,
        )
        user_input = ["Alice -> I love the weather today", "Alice", "exit"]
        current_time = datetime.now()
        mock_input.read_input.side_effect = user_input
        mock_clock.get_current_datetime.side_effect = [
            current_time - timedelta(minutes=5),
            current_time,
        ]

        cli.start()

        mock_printer.output.assert_called_with(
            "I love the weather today (5 minutes ago)"
        )
