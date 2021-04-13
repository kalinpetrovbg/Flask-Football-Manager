from players.skill_levels.skills import SKILL_LEVELS
import random

from players.player import Player


class Keeper(Player):
    def __init__(self, firs_name, last_name, age):
        super().__init__(firs_name, last_name, age)
        self.goalkeeping = None
        self.defending = None

    def generate_skills(self):
        stats = list(SKILL_LEVELS.items())
        self.goalkeeping = random.randint(8, 15)
        self.defending = random.randint(1, 10)


k = Keeper("Kalin", "Petrov", 28)
print(f"{k.first_name} {k.last_name} at {k.age} years")
k.generate_skills()
print(f"Goalkeeping: {k.goalkeeping}")
print(f"Defending: {k.defending}")
