class SocialNetworkAPI:
    def __init__(self, repo) -> None:
        self.repo = repo

    def post(self, user, message):
        self.repo.save_post(user, message)

    def read(self, user):
        self.repo.get_posts(user)

    def follows(self, follower, followee):
        raise NotImplementedError

    def wall(self, user):
        pass
