
from datetime import datetime, timedelta

from social_network.repo import Post


class Formatter:
    """
    Formatter class to format posts and time ago
    """

    def format_post(self, post: Post) -> str:
        return f"{post.message} ({self.__format_time_ago(post.timestamp)})"

    def format_posts(self, posts: list[Post]) -> str:
        return '\n'.join([self.format_post(post) for post in posts])

    def __format_time_ago(self, post_time: datetime) -> str:
        current_time = datetime.now()
        time_diff = current_time - post_time

        if time_diff < timedelta(minutes=1):
            return "just now"

        if time_diff < timedelta(hours=1):
            minutes = int(time_diff.total_seconds() // 60)
            return f"{minutes} minutes ago"

        if time_diff < timedelta(days=1):
            hours = int(time_diff.total_seconds() // 3600)
            return f"{hours} hours ago"

        days = time_diff.days
        return f"{days} days ago"
