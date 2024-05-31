import random

# Define constants
POPULATION_SIZE = 10000
MUTATION_RATE = 0.01
GENERATIONS = 1000
TARGET = 400
ERROR_THRESHOLD = 1e-6

# Generate initial population
def initialize_population(size):
    return [(random.randint(0, 50), random.randint(0, 50)) for _ in range(size)]

# Calculate fitness of an individual
def fitness(individual):
    x, y = individual
    return abs(3*x + 2*y - TARGET)

# Selection of parents based on fitness (tournament selection)
def selection(population):
    tournament_size = 5
    selected = random.sample(population, tournament_size)
    selected.sort(key=fitness)
    return selected[0], selected[1]

# Crossover between two parents to produce two children
def crossover(parent1, parent2):
    x1, y1 = parent1
    x2, y2 = parent2
    child1 = (x1, y2)
    child2 = (x2, y1)
    return child1, child2

# Mutation of an individual
def mutate(individual):
    x, y = individual
    if random.random() < MUTATION_RATE:
        x = random.randint(0, 50)
    if random.random() < MUTATION_RATE:
        y = random.randint(0, 50)
    return (x, y)

# Form the next generation
def next_generation(current_population):
    next_pop = []
    for _ in range(POPULATION_SIZE // 2):
        parent1, parent2 = selection(current_population)
        child1, child2 = crossover(parent1, parent2)
        child1 = mutate(child1)
        child2 = mutate(child2)
        next_pop.append(child1)
        next_pop.append(child2)
    return next_pop

# Main genetic algorithm
def genetic_algorithm():
    population = initialize_population(POPULATION_SIZE)
    for generation in range(GENERATIONS):
        population.sort(key=fitness)
        best_individual = population[0]
        best_fitness = fitness(best_individual)
        if best_fitness < ERROR_THRESHOLD:
            return best_individual, generation
        population = next_generation(population)
    population.sort(key=fitness)
    return population[0], GENERATIONS

solution, generations = genetic_algorithm()
print(f"Solution: x = {solution[0]}, y = {solution[1]} after {generations} generations.")
