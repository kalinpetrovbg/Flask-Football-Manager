from players.player import Player


class Midfielder(Player):
    def __init__(self, name, playmaking, passing, defending):
        super().__init__(name)
        self.playmaking = playmaking
        self.passing = passing
        self.defending = defending


    def generate_skills(self):
        pass
