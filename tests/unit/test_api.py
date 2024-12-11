from unittest import TestCase
from unittest.mock import Mock
from social_network.api import SocialNetworkAPI
from social_network.repo import SocialNetworkRepo
from social_network.clock import Clock
from social_network.formatter import Formatter


class TestSocialNetworkAPI(TestCase):
    def setUp(self):
        self.mock_clock = Mock(Clock)
        self.repo = Mock(SocialNetworkRepo)
        self.formatter = Mock(Formatter)
        self.api = SocialNetworkAPI(self.repo, self.formatter)

    def test_api_post(self):
        self.api.post("Chris", "Hello, World!")

        self.api.repo.save_post.assert_called_with("Chris", "Hello, World!")

    def test_api_read(self):
        self.api.read("Chris")

        self.api.repo.get_posts.assert_called_with("Chris")

    def test_api_follows(self):
        self.api.follows("Chris", "Alice")

        self.api.repo.follow_user.assert_called_with("Chris", "Alice")

    def test_api_wall(self):
        self.api.wall("Chris")

        self.api.repo.get_wall.assert_called_with("Chris")
