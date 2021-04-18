from players.player import Player


class Defender(Player):
    def __init__(self, name):
        super().__init__(name)
        self.defending = None
        self.passing = None
        self.playmaking = None

    def generate_skills(self):
        pass
