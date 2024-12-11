from social_network.repo import User, SocialNetworkRepo
from social_network.formatter import Formatter


class SocialNetworkAPI:
    """
    Social Network API class to post, read, follow and get wall
    """

    def __init__(self, repo: SocialNetworkRepo, formatter: Formatter) -> None:
        self.repo = repo
        self.formatter = formatter

    def post(self, user: User, message: str) -> None:
        self.repo.save_post(user, message)

    def read(self, user: User) -> str:
        posts = self.repo.get_posts(user)
        return self.formatter.format_posts(posts)

    def follows(self, follower: User, followee: User) -> None:
        self.repo.follow_user(follower, followee)

    def wall(self, user: User) -> str:
        return self.repo.get_wall(user)
