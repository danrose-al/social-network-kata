from social_network.clock import Clock
from social_network.repo import SocialNetworkRepo

class SocialNetworkAPI:
    def __init__(self, clock=None, repo=None) -> None:
        self.clock = clock or Clock()
        self.repo = repo or SocialNetworkRepo()

    def post(self, user, message):
        self.repo.save_post(user, message)

    def read(self, user):
        self.repo.get_posts(user)

    def follows(self, follower, followee):
        raise NotImplementedError

    def wall(self, user):
        pass
