from unittest import TestCase
from unittest.mock import Mock
from social_network.api import SocialNetworkAPI
from social_network.social_network_repo import SocialNetworkRepo
from social_network.post import Post
from social_network.user import User
from social_network.clock import Clock


class TestSocialNetworkAPI(TestCase):
    def test_api_post(self):
        # Arrange
        mock_clock = Mock(Clock)
        repo = Mock(SocialNetworkRepo)
        api = SocialNetworkAPI(clock=mock_clock, social_network_repo=repo)
        user = User("Chris")
        # posts = Posts()
        # api.users.get_user("Chris").posts
        api.post("Chris", "Hello, World!")

        social_network_repo.add_post.called_with("Chris", "Hello, World!")
        # post create a new post for the user
        # something needs to keep track of it

        # Assert that the post we created is in the list of posts for that user

        # user_input = "Chris -> Hello, World!"
        # message = Message(user_input, mock_clock.now())
        # user = User("Chris")
        # PostsAPI -> PostsDB (mock the return / side effect)
        # UsersAPI -> UsersDB (mock the side effect)
        # take the name, message
        # do something with it
        # check that it did what its supposed to do

        # called stuff
        # returns nothing (status)

        # # Act
        # api.post(post)

        # # Assert
        # self.assertIn(post, api.posts)
