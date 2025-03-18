import random
import numpy as np

job_times = [2, 4, 6, 8, 3, 5]
machines = 3
population_size = 10
generations = 100

def initialize_population(jobs, machines, pop_size):
    return [np.array([(j, random.randint(0, machines - 1)) for j in range(len(jobs))]) for _ in range(pop_size)]

def fitness(chromosome):
    loads = [0] * machines
    for job_id, machine_id in chromosome:
        loads[machine_id] += job_times[job_id]
    return 1 / (sum([l**2 for l in loads]) + 0.01)

def crossover(parent1, parent2):
    cut1, cut2 = sorted(random.sample(range(len(parent1)), 2))
    child1 = np.concatenate((parent1[:cut1], parent2[cut1:cut2], parent1[cut2:]))
    child2 = np.concatenate((parent2[:cut1], parent1[cut1:cut2], parent2[cut2:]))
    return child1, child2

def mutate(chromosome):
    idx = random.randint(0, len(chromosome) - 1)
    chromosome[idx] = (chromosome[idx][0], random.randint(0, machines - 1))
    return chromosome

def roulette_selection(population, fitnesses):
    total = sum(fitnesses)
    pick = random.uniform(0, total)
    current = 0
    for chrom, fit in zip(population, fitnesses):
        current += fit
        if current > pick:
            return chrom

population = initialize_population(job_times, machines, population_size)

for _ in range(generations):
    fitnesses = [fitness(chrom) for chrom in population]
    new_pop = []
    for _ in range(population_size // 2):
        p1 = roulette_selection(population, fitnesses)
        p2 = roulette_selection(population, fitnesses)
        c1, c2 = crossover(p1, p2)
        c1, c2 = mutate(c1), mutate(c2)
        new_pop.extend([c1, c2])
    population = new_pop

best = max(population, key=lambda c: fitness(c))
print("Best job schedule assignments (job_id, machine_id):")
print(best)
