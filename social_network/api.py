from datetime import datetime, timedelta

class SocialNetworkAPI:
    def __init__(self, repo) -> None:
        self.repo = repo

    def post(self, user, message):
        self.repo.save_post(user, message)

    def read(self, user):
        posts = self.repo.get_posts(user)
        return "\n".join([f"{user} - {post.message} {timedelta(post.timestamp)}" for post in posts])

    def follows(self, follower, followee):
        self.repo.follow_user(follower, followee)

    def wall(self, user):
        self.repo.get_wall(user)
