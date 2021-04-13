from players.player import Player


class Winger(Player):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.playmaking = None
        self.passing = None
        self.defending = None
        self.winger = None
        self.scoring = None

    def generate_skills(self):
        pass