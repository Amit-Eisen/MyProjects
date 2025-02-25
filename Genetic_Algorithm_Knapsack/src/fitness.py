# Constants
WEIGHT_LIMIT = 100

def fitness(solution, instruments):
    """
    Calculates the fitness of a given solution.
    Returns (total profit, total weight).
    """
    total_profit = 0
    total_weight = 0
    for i in range(len(solution)):
        if solution[i] == 1:
            total_profit += instruments[i][0]
            total_weight += instruments[i][1]
        if total_weight >= WEIGHT_LIMIT:
            total_profit = 0
            break
    return total_profit, total_weight
