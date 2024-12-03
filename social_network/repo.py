from social_network.post import Post
from dataclasses import dataclasses

@dataclasses
class User:
    username: str
    posts: list[Post]

class SocialNetworkRepo:
    def __init__(self):
        pass

    def save_post(self, post):
        raise NotImplementedError
