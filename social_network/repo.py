from dataclasses import dataclass

from datetime import datetime


@dataclass
class Post:
    message: str
    timestamp: datetime


@dataclass
class User:
    name: str
    posts: list[Post]


class SocialNetworkRepo:
    def __init__(self, clock):
        self.clock = clock
        self.users = {}

    def save_post(self, username, message):
        post = Post(message, self.clock.get_current_datetime())

        if username not in self.users:
            user = User(username, [post])
            self.users[username] = user
        else:
            user = self.users[username]
            user.posts.append(post)

    def get_posts(self, user):
        pass

    def follow_user(self, follower, followee):
        pass

    def get_wall(self, user):
        pass
