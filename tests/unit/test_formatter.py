from datetime import timedelta, datetime
from unittest import TestCase
from social_network.formatter import Formatter
from social_network.repo import Post


class TestFormater(TestCase):
    def setUp(self):
        self.formatter = Formatter()

    def test_format_post_now(self):
        test_post = Post("This is some message")

        formatted_post = self.formatter.format_post(test_post)

        self.assertEqual(formatted_post, "This is some message (just now)")


    def test_format_posts(self):
        current_time = datetime.now()

        posts = [
            Post("My milkshake", current_time - timedelta(minutes=5)),
            Post("Brings all the boys", current_time - timedelta(hours=5)),
            Post("To the yard", current_time - timedelta(days=5)),
            Post("Dam right!")
        ]

        formatted_posts = self.formatter.format_posts(posts)
        self.assertEqual(formatted_posts, "My milkshake (5 minutes ago)\nBrings all the boys (5 hours ago)\nTo the yard (5 days ago)\nDam right! (just now)")
