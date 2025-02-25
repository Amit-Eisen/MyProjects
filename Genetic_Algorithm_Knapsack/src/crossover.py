import numpy as np

# Constants
ALPHA = 0.5


def mate_parents(parents_list):
    """
    Performs crossover using the head-tail method.
    """
    parent_a = parents_list[0].tolist()
    parent_b = parents_list[1].tolist()

    head_a = parent_a[:int(len(parent_a) * ALPHA)]
    tail_a = parent_a[int(len(parent_a) * ALPHA):]
    head_b = parent_b[:int(len(parent_b) * ALPHA)]
    tail_b = parent_b[int(len(parent_b) * ALPHA):]

    offspring_1 = head_a + tail_b
    offspring_2 = head_b + tail_a
    return np.array([offspring_1, offspring_2])
