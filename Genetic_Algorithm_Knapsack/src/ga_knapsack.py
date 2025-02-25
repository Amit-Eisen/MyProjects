import numpy as np
import matplotlib.pyplot as plt
from data_loader import load_data
from fitness import fitness
from selection import mating_selection
from crossover import mate_parents
from mutation import mutate_offspring

# Constants
N_POPULATION = 10
GENERATIONS = 1000
fitness_history = []

def generate_population(num_items):
    """Generates an initial random population."""
    return np.random.randint(2, size=(N_POPULATION, num_items))

def solve():
    """Runs the Genetic Algorithm."""
    instruments = load_data()
    population = generate_population(len(instruments))
    best_solution = None
    best_solution_profit = None
    best_solution_iteration = 0
    best_solution_weight = 0

    for i in range(GENERATIONS):
        fitness_scores = np.array([fitness(ind, instruments)[0] for ind in population])
        max_fitness_idx = np.argmax(fitness_scores)

        if best_solution_profit is None or fitness_scores[max_fitness_idx] > best_solution_profit:
            best_solution_profit = fitness_scores[max_fitness_idx]
            best_solution_iteration = i
            best_solution = population[max_fitness_idx]
            best_solution_weight = fitness(best_solution, instruments)[1]

        parents = mating_selection(population, fitness_scores)
        offspring = mate_parents(parents)
        mutated = mutate_offspring(offspring)

        population = np.vstack([parents, offspring, mutated])
        fitness_history.append(best_solution_profit)

    print(f"GA found the best solution after {best_solution_iteration} iterations")
    print(f"Expected profit: {best_solution_profit}$")
    print(f"Total weight {best_solution_weight} Kg")

    plt.plot(fitness_history)
    plt.xlabel("Generation")
    plt.ylabel("Fitness")
    plt.show()

if __name__ == "__main__":
    solve()
