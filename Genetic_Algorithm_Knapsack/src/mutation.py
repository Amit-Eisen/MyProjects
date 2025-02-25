import numpy as np
import random

# Constants
MUTATION_RATE = 0.2


def mutate_offspring(offsprings):
    """
    Applies mutation by swapping two genes randomly.
    """
    offspring_num = random.randint(0, 1)
    offspring = offsprings[offspring_num]

    for _ in range(int(len(offspring) * MUTATION_RATE)):
        a, b = np.random.randint(0, len(offspring), size=2)
        offspring[a], offspring[b] = offspring[b], offspring[a]

    return np.array(offspring)
