from players.skill_levels.skills import SKILL_LEVELS
from players.player_names.names_data import *
import random

from players.player import Player


class Keeper(Player):
    goalkeeping = None

    def __init__(self, name):
        super().__init__(name)
        self.defending = None

    def generate_skills(self):
        self.goalkeeping = random.randint(8, 15)
        self.defending = random.randint(1, 10)


# k = Keeper("Player 1")
# print(k.name)
# k.generate_skills()
# print(k.goalkeeping)