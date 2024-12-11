from dataclasses import dataclass, field

from datetime import datetime

from social_network.clock import Clock


@dataclass
class Post:
    """
    Post class to store post information
    """
    message: str
    timestamp: datetime = datetime.now()


@dataclass
class User:
    """
    User class to store user information
    """
    name: str
    posts: list[Post] = field(default_factory=list)
    following: list[str] = field(default_factory=list)


class SocialNetworkRepo:
    """
    Social Network Repository class to save and retrieve posts
    """
    def __init__(self, clock: Clock) -> None:
        self.clock = clock
        self.users = {}

    def __create_user(self, username: str) -> None:
        if username not in self.users:
            user = User(username)
            self.users[username] = user

    def save_post(self, username: str, message: str) -> None:
        self.__create_user(username)
        post = Post(message, self.clock.get_current_datetime())

        user = self.users[username]
        user.posts.append(post)

    def get_posts(self, username: str) -> list[Post] :
        self.__create_user(username)

        return self.users[username].posts

    def follow_user(self, follower: User, followee: User) -> None:
        self.__create_user(follower)

        self.users[follower].following.append(followee)

    def get_wall(self, user: User) -> list[Post]:
        raise NotImplementedError
