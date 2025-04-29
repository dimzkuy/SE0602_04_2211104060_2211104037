import random
from config import POP_SIZE, GENOME_LENGTH, GEN_MAX, PC, PM
from utils import decode, fitness

def init_pop():
    return [''.join(random.choice('01') for _ in range(GENOME_LENGTH)) for _ in range(POP_SIZE)]

def select(pop, scores):
    i, j = random.sample(range(POP_SIZE), 2)
    return pop[i] if scores[i] < scores[j] else pop[j]

def crossover(p1, p2):
    if random.random() < PC:
        point = random.randint(1, GENOME_LENGTH - 1)
        return p1[:point] + p2[point:], p2[:point] + p1[point:]
    return p1, p2

def mutate(chrom):
    return ''.join(bit if random.random() > PM else '1' if bit == '0' else '0' for bit in chrom)

def run_ga():
    pop = init_pop()
    for _ in range(GEN_MAX):
        decoded = [decode(c) for c in pop]
        scores = [fitness(x1, x2) for x1, x2 in decoded]
        next_gen = [pop[scores.index(min(scores))]]  # elitisme
        while len(next_gen) < POP_SIZE:
            p1, p2 = select(pop, scores), select(pop, scores)
            c1, c2 = crossover(p1, p2)
            next_gen.extend([mutate(c1), mutate(c2)])
        pop = next_gen[:POP_SIZE]
    # Output akhir
    decoded = [decode(c) for c in pop]
    scores = [fitness(x1, x2) for x1, x2 in decoded]
    best = scores.index(min(scores))
    return pop[best], decoded[best], scores[best]
