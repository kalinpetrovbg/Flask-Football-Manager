from players.player import Player


class Defender(Player):
    def __init__(self, firs_name, last_name, age):
        super().__init__(firs_name, last_name, age)
        self.defending = None
        self.passing = None
        self.playmaking = None

    def generate_skills(self):
        pass
