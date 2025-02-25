import random
import numpy as np


def mating_selection(population, fitness_scores):
    """
    Uses tournament selection to pick two parents.
    """
    parents_list = []
    random.shuffle(population)
    if fitness_scores[0] > fitness_scores[1]:
        parents_list.append(population[0])
    else:
        parents_list.append(population[1])

    if fitness_scores[2] > fitness_scores[3]:
        parents_list.append(population[2])
    else:
        parents_list.append(population[3])

    return np.array(parents_list)
