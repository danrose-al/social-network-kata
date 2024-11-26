from unittest import TestCase

class TestSocialNetworkAPI(TestCase):
    def test_api_post(self):
        # Arrange
        mock_clock = Mock(Clock)
        api = SocialNetworkAPI(
            clock=mock_clock
        )        
        post = Post("Hello, World!")
        user = SocialNetworkUser()
        api.post(user, message)

        # # Act
        # api.post(post)

        # # Assert
        # self.assertIn(post, api.posts)