from social_network.api import SocialNetworkAPI

class ParseInput:
    def __init__(self, social_network_api = None):
        self.social_network_api = social_network_api or SocialNetworkAPI() 

    def process(self, user_input: str) -> None:
        if "->" in user_input:
            split_list = [data.strip() for data in user_input.split("->")]
            user, message = split_list[0], split_list[1]
            self.social_network_api.post(user, message)
        elif len(user_input.split(' ')) == 1:
            user = user_input
            self.social_network_api.read(user)
        elif "follows" in user_input:
            split_list = [data.strip() for data in user_input.split("follows")]
            follower, followee = split_list[0], split_list[1]
            self.social_network_api.follows(follower, followee)
        elif "wall" in user_input:
            user = user_input.replace("wall", "").strip()
            self.social_network_api.wall(user)


