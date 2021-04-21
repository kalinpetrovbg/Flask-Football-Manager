from players.player import Player


class Keeper(Player):
    def __init__(self, name, goalkeeping, defending):
        super().__init__(name)
        self.goalkeeping = goalkeeping
        self.defending = defending

    def generate_skills(self):
        pass
