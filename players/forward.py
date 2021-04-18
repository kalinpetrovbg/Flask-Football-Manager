from players.player import Player


class Forward(Player):
    def __init__(self, name):
        super().__init__(name)
        self.scoring = None
        self.passing = None
        self.winger = None

    def generate_skills(self):
        pass
