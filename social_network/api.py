from social_network.clock import Clock

class SocialNetworkAPI:

    def __init__(self, clock = None) -> None:
        self.clock = clock or Clock()
        