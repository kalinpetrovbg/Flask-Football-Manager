from players.player import Player


class Defender(Player):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.defending = None
        self.passing = None
        self.playmaking = None

    def generate_skills(self):
        pass
