from players.skill_levels.skills import SKILL_LEVELS
import random

class Player:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.experience = 0

    def calculate_experience(self):
        pass

    def generate_skills(self):
        pass
        # stats = list(SKILL_LEVELS.items())
        # self.goalkeeping = random.choice(stats)
        # self.defending = random.choice(stats)
