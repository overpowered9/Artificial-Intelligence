import random

# Constants
POPULATION_SIZE = 100
GENERATIONS = 1000
MUTATION_RATE = 0.01
ERROR_THRESHOLD = 2

# Target equation constants
TARGET = 69
COEFF_X = 3
COEFF_Y = 2

def initialize_population(size):
    population = []
    for _ in range(size):
        x = random.randint(0, TARGET)
        y = random.randint(0, TARGET)
        population.append((x, y))
    return population

def fitness(individual):
    x, y = individual
    return abs(COEFF_X * x + COEFF_Y * y - TARGET)

def selection(population):
    population = sorted(population, key=lambda x: fitness(x))
    return population[:POPULATION_SIZE // 2]

def crossover(parent1, parent2):
    child1 = (parent1[0], parent2[1])
    child2 = (parent2[0], parent1[1])
    return child1, child2

def mutate(individual):
    x, y = individual
    if random.random() < MUTATION_RATE:
        x = random.randint(0, TARGET)
    if random.random() < MUTATION_RATE:
        y = random.randint(0, TARGET)
    return (x, y)

def evolve(population):
    new_generation = []
    selected = selection(population)
    while len(new_generation) < POPULATION_SIZE:
        parent1 = random.choice(selected)
        parent2 = random.choice(selected)
        child1, child2 = crossover(parent1, parent2)
        new_generation.append(mutate(child1))
        new_generation.append(mutate(child2))
    return new_generation

def genetic_algorithm():
    population = initialize_population(POPULATION_SIZE)
    for generation in range(GENERATIONS):
        population = evolve(population)
        best_individual = min(population, key=lambda x: fitness(x))
        best_fitness = fitness(best_individual)
        print(f"Generation {generation}: Best fitness {best_fitness} with x = {best_individual[0]}, y = {best_individual[1]}")
        if best_fitness <= ERROR_THRESHOLD:
            break
    return best_individual

solution = genetic_algorithm()
print(f"Solution found: x = {solution[0]}, y = {solution[1]}, fitness = {fitness(solution)}")
