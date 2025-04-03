import random

class RandomSelector:
    def __init__(self, num_arms):
        self.num_arms = num_arms

    def select_arm(self):
        return random.randint(0, self.num_arms - 1)

    def update(self, chosen_arm, reward):
        pass  # Random selection has no learning
