from players.player import Player


class Forward(Player):
    def __init__(self, name, scoring, passing, playmaking):
        super().__init__(name)
        self.scoring = scoring
        self.passing = passing
        self.playmaking = playmaking

    def generate_skills(self):
        pass
