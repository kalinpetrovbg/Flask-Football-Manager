from players.player import Player


class Forward(Player):
    def __init__(self, firs_name, last_name, age):
        super().__init__(firs_name, last_name, age)
        self.scoring = None
        self.passing = None
        self.winger = None

    def generate_skills(self):
        pass
