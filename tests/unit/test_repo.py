from unittest import TestCase
from unittest.mock import Mock

from datetime import datetime

from social_network.repo import SocialNetworkRepo, Post
from social_network.clock import Clock


class TestSocialNetworkRepo(TestCase):
    def test_repo_put(self):
        # Arrange
        mock_clock = Mock(Clock)
        repo = SocialNetworkRepo(mock_clock)
        current_time = datetime.now()
        mock_clock.get_current_datetime.return_value = current_time

        repo.save_post("Chris", "Hello, World!")

        assert repo.users["Chris"].posts == [Post("Hello, World!", current_time)]
