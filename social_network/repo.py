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

    def __create_user(self, username):
        if username not in self.users:
            user = User(username, [])
            self.users[username] = user

    def save_post(self, username, message):
        self.__create_user(username)
        post = Post(message, self.clock.get_current_datetime())

        user = self.users[username]
        user.posts.append(post)

    def get_posts(self, username):
        self.__create_user(username)

        return self.users[username].posts

    def follow_user(self, follower, followee):
        pass

    def get_wall(self, user):
        pass
