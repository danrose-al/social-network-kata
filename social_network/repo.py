from social_network.post import Post


class User:
    username: str
    posts: list[Post]


class SocialNetworkRepo:
    def __init__(self):
        pass

    def save_post(self, user, message):
        pass

    def get_posts(self, user):
        pass
