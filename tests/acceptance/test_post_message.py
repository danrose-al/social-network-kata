from unittest import TestCase
from unittest.mock import patch, Mock

from datetime import datetime, timedelta

from social_network.input_wrapper import InputWrapper
from social_network.print_wrapper import PrintWrapper
from social_network.clock import Clock

class TestPostMessage(TestCase):

    def test_user_can_post_and_read_a_message(self):
        mock_input = Mock(InputWrapper)
        mock_printer = Mock(PrintWrapper)
        mock_clock = Mock(Clock)
        cli = SocialNetworkCLI(input_wrapper=mock_input, clock=mock_clock, print_wrapper=mock_printer)
        user_input = ['Alice -> I love the weather today', "Read Alice"]
        current_time = datetime.now()
        mock_clock.get_date_and_time.side_effect = [current_time - timedelta(minutes=5), current_time]
        mock_input.read_input.side_effect = user_input

        cli.start()

        mock_printer.output.assert_called_with("I love the weather today (5 minutes ago)")



    ### THIS IS TO NOT LOSE THE STRING OF THE
    # def test_user_can_post_message_to_timeline(self):
    #     # Given
    #     mock_input = Mock(InputWrapper)
    #     mock_printer = Mock(PrintWrapper)
    #     mock_clock = Mock(Clock)
    #     cli = SocialNetworkCLI(input_wrapper=mock_input, clock=mock_clock, print_wrapper=mock_printer)
    #     user_input_1 = 'Alice -> I love the weather today'
    #     user_input_2 = "Charlie -> I'm in New York today! Anyone wants to have a coffee?"
    #     user_input_3 = "Charlie follows Alice"
    #     user_input_4 = "Charlie wall"
    #OPUTPUT = Charlie - I'm in New York today! Anyone wants to have a coffee? (15 seconds ago)\nAlice - I love the weather today (5 minutes ago)
