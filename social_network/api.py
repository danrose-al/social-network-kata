class SocialNetworkAPI:
    def __init__(self, repo) -> None:
        self.repo = repo

    def post(self, user, message):
        self.repo.save_post(user, message)

    def read(self, user):
        pass

    def follows(self, follower, followee):
        pass

    def wall(self, user):
        pass
