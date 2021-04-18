from players.player import Player


class Midfielder(Player):
    def __init__(self, name):
        super().__init__(name)
        self.playmaking = None
        self.passing = None
        self.defending = None
        self.winger = None

    def generate_skills(self):
        pass
