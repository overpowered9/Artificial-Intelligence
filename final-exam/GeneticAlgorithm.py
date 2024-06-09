import random

#########################
Size_of_Population = 70
Mutation_Rate = 0.01
GENERATIONS = 1000
TARGET = 50
Error_Thresh_Hold = 2

#########################
def initialize_population1(size):
    population = []
    for _ in range(size):
        x = random.randint(0, TARGET)
        y = random.randint(0, TARGET)
        population.append((x, y))
    return population
#A better alternate using listcomprehension,
def initialize_population(size):
    return [(random.randint(0, TARGET), random.randint(0, TARGET)) for _ in range(size)]

def fitness(individual):
    x, y = individual
    return abs(3*x + 2*y - TARGET)

def parent_selection(population):
    tournament_size = 5
    selected = random.sample(population, tournament_size)
    selected.sort(key=fitness)
    return selected[0], selected[1]

#Crossover
def crossover(parent1, parent2):
    x1, y1 = parent1
    x2, y2 = parent2
    child1 = (x1, y2)
    child2 = (x2, y1)
    return child1, child2

def mutaion(individual):
    x, y = individual
    if random.random() < Mutation_Rate:
        x = random.randint(0, 50)
    if random.random() < Mutation_Rate:
        y = random.randint(0, 50)
    return (x, y)

def next_generation(current_population):
    new_pop = []
    for _ in range(Size_of_Population // 2):
        parent1, parent2 = parent_selection(current_population)
        child1, child2 = crossover(parent1, parent2)
        child1 = mutaion(child1)
        child2 = mutaion(child2)
        new_pop.append(child1)
        new_pop.append(child2)
    return new_pop
#genteic algorithm
def geneti_algo():
    population = initialize_population(Size_of_Population)
    for generation in range(GENERATIONS):
        population.sort(key=fitness)
        best_individual = population[0]
        best_fitness = fitness(best_individual)
        ###Question2,last part Conversion check###
        if best_fitness < Error_Thresh_Hold:
            return best_individual, generation
        population = next_generation(population)
    population.sort(key=fitness)
    return population[0], GENERATIONS

solution, generations = geneti_algo()
print(f"Solution: x = {solution[0]}, y = {solution[1]} after {generations} generations.")
