import random

class ThompsonSampler:
    def __init__(self, num_arms):
        self.num_arms = num_arms
        self.successes = [0] * num_arms
        self.failures = [0] * num_arms

    def select_arm(self):
        max_beta = -1
        chosen_arm = 0
        for i in range(self.num_arms):
            beta = random.betavariate(self.successes[i] + 1, self.failures[i] + 1)
            if beta > max_beta:
                max_beta = beta
                chosen_arm = i
        return chosen_arm

    def update(self, chosen_arm, reward):
        if reward == 1:
            self.successes[chosen_arm] += 1
        else:
            self.failures[chosen_arm] += 1
