from social_network.clock import Clock


class SocialNetworkAPI:
    def __init__(self, clock=None, repo=None) -> None:
        self.clock = clock or Clock()
        self.repo = repo

    def post(self, user, message):
        self.repo.save_post(user, message)
