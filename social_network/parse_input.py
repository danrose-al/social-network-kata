from social_network.api import SocialNetworkAPI

class ParseInput:
    def __init__(self, social_network_api = None):
        self.social_network_api = social_network_api or SocialNetworkAPI() 

    def process(self, input: str) -> None:
        if "->" in input:
            split_list = [data.strip() for data in input.split("->")]
            user, message = split_list[0], split_list[1]
            self.social_network_api.post(user, message)
        elif len(input.split(' ')) == 1:
            user = input
            self.social_network_api.read(user)
        elif "follows" in input:
            split_list = [data.strip() for data in input.split("follows")]
            follower, followee = split_list[0], split_list[1]
            self.social_network_api.follows(follower, followee)
        elif "wall" in input:
            user = input.replace("wall", "").strip()
            self.social_network_api.wall(user)


