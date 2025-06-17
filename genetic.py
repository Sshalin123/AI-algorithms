import random

# Fitness function: f(x) = x² - 3x + 5
def fitness(x):
    return x ** 2 - 3 * x + 5

# Binary encoding (5 bits since 0–31)
def encode(x):
    return format(x, '05b')

def decode(binary):
    return int(binary, 2)

# Generate initial population
def generate_population(size):
    return [random.randint(0, 31) for _ in range(size)]

# Selection (roulette wheel based on fitness)
def select(population):
    fitness_vals = [fitness(x) for x in population]
    total = sum(fitness_vals)
    probs = [f / total for f in fitness_vals]
    return random.choices(population, weights=probs, k=2)

# Single-point crossover
def crossover(p1, p2):
    b1 = encode(p1)
    b2 = encode(p2)
    point = random.randint(1, 4)
    child1 = decode(b1[:point] + b2[point:])
    child2 = decode(b2[:point] + b1[point:])
    return child1, child2

# Mutation (bit flip)
def mutate(x, mutation_rate=0.1):
    b = list(encode(x))
    for i in range(len(b)):
        if random.random() < mutation_rate:
            b[i] = '1' if b[i] == '0' else '0'
    return decode(''.join(b))

# Main genetic algorithm function
def genetic_algorithm():
    population = generate_population(4)
    print("Initial population:", population)

    for gen in range(2):
        print(f"\n--- Generation {gen + 1} ---")

        # Selection
        parent1, parent2 = select(population)
        print("Selected parents:", parent1, parent2)

        # Crossover
        child1, child2 = crossover(parent1, parent2)
        print("Children before mutation:", child1, child2)

        # Mutation
        child1 = mutate(child1)
        child2 = mutate(child2)
        print("Children after mutation:", child1, child2)

        # new population 
        population += [child1, child2]
        population = sorted(population, key=fitness, reverse=True)[:4]
        print("New population:", population)

    best = max(population, key=fitness)
    print("\n Best solution found: x =", best, "→ f(x) =", fitness(best))


genetic_algorithm()
