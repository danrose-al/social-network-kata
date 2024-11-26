from unittest import TestCase
from unittest.mock import Mock

from social_network.parse_input import ParseInput
from social_network.api import SocialNetworkAPI

class TestParseInput(TestCase):

    def test_traslation_of_string_post(self):
        mock_social_network_api = Mock(SocialNetworkAPI)
        parse_input = ParseInput(social_network_api = mock_social_network_api)

        parse_input.process("Alice -> I love the weather today")

        mock_social_network_api.post.assert_called_once_with('Alice', 'I love the weather today')
    
    def test_translation_of_string_read(self):
        mock_social_network_api = Mock(SocialNetworkAPI)
        parse_input = ParseInput(social_network_api = mock_social_network_api)

        parse_input.process("Alice")

        mock_social_network_api.read.assert_called_once_with("Alice")
    
    def test_translation_of_string_follow(self):
        mock_social_network_api = Mock(SocialNetworkAPI)
        parse_input = ParseInput(social_network_api = mock_social_network_api)

        parse_input.process("Charlie follows Alice")
        
        mock_social_network_api.follows.assert_called_once_with("Charlie", "Alice")
    
    def test_translation_of_string_wall(self):
        mock_social_network_api = Mock(SocialNetworkAPI)
        parse_input = ParseInput(social_network_api = mock_social_network_api)

        parse_input.process("Charlie wall")
        
        mock_social_network_api.wall.assert_called_once_with("Charlie")




    # def test_call_api_with_command(self):
    #     pass
