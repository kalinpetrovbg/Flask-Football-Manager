from players.skill_levels.skills import SKILL_LEVELS
from players.player_names.names_data import *
import random

class Player:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.experience = 0

    def calculate_experience(self):
        pass

    def generate_skills(self):
        pass
        # stats = list(SKILL_LEVELS.items())
        # self.goalkeeping = random.choice(stats)
        # self.defending = random.choice(stats)
