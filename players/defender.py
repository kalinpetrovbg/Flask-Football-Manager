from players.player import Player


class Defender(Player):
    def __init__(self, name, defending, passing, playmaking):
        super().__init__(name)
        self.defending = defending
        self.passing = passing
        self.playmaking = playmaking

    def generate_skills(self):
        pass


