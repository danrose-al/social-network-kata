from social_network.clock import Clock


class SocialNetworkAPI:
    def __init__(self, clock=None) -> None:
        self.clock = clock or Clock()
        self.users_repo
        self.users_repo.get_users_posts("chris")
        self.users = []
        self.posts

    def post(self, user, message):
        pass
