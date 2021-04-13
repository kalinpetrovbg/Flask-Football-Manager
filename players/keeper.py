from players.skill_levels.skills import SKILL_LEVELS
from players.player_names.names_data import *
import random

from players.player import Player


class Keeper(Player):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.goalkeeping = None
        self.defending = None

    def generate_skills(self):
        self.goalkeeping = random.randint(8, 15)
        self.defending = random.randint(1, 10)


k = Keeper("Kalin", "Petrov", 28)
print(f"{k.name}  at {k.age} years")
k.generate_skills()
print(f"Goalkeeping: {k.goalkeeping}")
print(f"Defending: {k.defending}")
