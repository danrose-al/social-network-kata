
from social_network.api import SocialNetworkAPI


class ParseInput:
    """
    ParseInput class is responsible for processing user input and calling the appropriate method from the SocialNetworkAPI
    """

    def __init__(self, social_network_api: SocialNetworkAPI) -> None:
        self.social_network_api = social_network_api

    def __process_post(self, user_input: str) -> str:
        split_list = [data.strip() for data in user_input.split("->")]
        user, message = split_list[0], split_list[1]
        return self.social_network_api.post(user, message)

    def __process_read(self, user_input: str) -> str:
        user = user_input
        return self.social_network_api.read(user)

    def __process_follows(self, user_input: str) -> str:
        split_list = [data.strip() for data in user_input.split("follows")]
        follower, followee = split_list[0], split_list[1]
        return self.social_network_api.follows(follower, followee)

    def __process_wall(self, user_input: str) -> str:
        user = user_input.replace("wall", "").strip()
        return self.social_network_api.wall(user)

    def process(self, user_input: str) -> str | None:
        if "->" in user_input:
            return self.__process_post(user_input)

        input_len = len(user_input.split(" "))

        if input_len == 1:
            return self.__process_read(user_input)

        if "follows" in user_input:
            return self.__process_follows(user_input)

        if "wall" in user_input:
            return self.__process_wall(user_input)
