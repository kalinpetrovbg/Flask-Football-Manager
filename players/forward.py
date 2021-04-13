from players.player import Player


class Forward(Player):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.scoring = None
        self.passing = None
        self.winger = None

    def generate_skills(self):
        pass
