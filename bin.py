import random

item_sizes = [4, 8, 1, 4, 2, 1]
bin_capacity = 10
population_size = 10
generations = 100

def initialize_population(items, pop_size):
    population = []
    for _ in range(pop_size):
        bins = [[]]
        for size in items:
            placed = False
            for b in bins:
                if sum(b) + size <= bin_capacity:
                    b.append(size)
                    placed = True
                    break
            if not placed:
                bins.append([size])
        population.append(bins)
    return population

def fitness(bins):
    used_bins = len(bins)
    waste = sum(bin_capacity - sum(b) for b in bins)
    return 1 / (used_bins + (waste / 100) + 0.01)

def crossover(parent1, parent2):
    cut = random.randint(1, min(len(parent1), len(parent2)) - 1)
    child1 = parent1[:cut] + parent2[cut:]
    child2 = parent2[:cut] + parent1[cut:]
    return child1, child2

def mutate(bins):
    if len(bins) < 2:
        return bins
    from_bin = random.choice(bins)
    if not from_bin:
        return bins
    item = random.choice(from_bin)
    from_bin.remove(item)
    placed = False
    for b in bins:
        if sum(b) + item <= bin_capacity:
            b.append(item)
            placed = True
            break
    if not placed:
        bins.append([item])
    return bins

def roulette_selection(pop, fitnesses):
    total = sum(fitnesses)
    pick = random.uniform(0, total)
    current = 0
    for chrom, fit in zip(pop, fitnesses):
        current += fit
        if current > pick:
            return chrom

population = initialize_population(item_sizes, population_size)

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
print("Best bin arrangement found:")
for i, b in enumerate(best):
    print(f"Bin {i+1}: {b} (Used {sum(b)}/{bin_capacity})")
