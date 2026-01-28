import random
import numpy as np

def calculate_cycle_length(cycle, graph, costs):
    length = 0
    for i in range(len(cycle)):
        u, v = cycle[i], cycle[(i + 1) % len(cycle)]
        length += costs[u]
        for j, w in graph[u]:
            if j == v:
                length += w
                break
    return length

def create_initial_population(graph, population_size):
    population = []
    V = len(graph)
    for _ in range(population_size):
        cycle = list(range(V))
        random.shuffle(cycle)
        population.append(cycle)
    return population

def select_best_population(population, graph, costs, selection_size):
    population_scores = [(cycle, calculate_cycle_length(cycle, graph, costs)) for cycle in population]
    population_scores.sort(key=lambda x: x[1])
    return [cycle for cycle, score in population_scores[:selection_size]]

def crossover(parent1, parent2):
    size = len(parent1)
    start, end = sorted(random.sample(range(size), 2))
    child = [None]*size
    child[start:end+1] = parent1[start:end+1]
    
    ptr = end+1
    for vertex in parent2:
        if vertex not in child:
            if ptr >= size:
                ptr = 0
            while child[ptr] is not None:
                ptr += 1
            child[ptr] = vertex
    return child

def mutate(cycle):
    size = len(cycle)
    u, v = sorted(random.sample(range(size), 2))
    cycle[u], cycle[v] = cycle[v], cycle[u]
    

def genetic_algorithm(graph, costs, population_size=100, generations=500, mutation_rate=0.05, selection_size=20):
    population = create_initial_population(graph, population_size)
    
    for _ in range(generations):
        new_population = select_best_population(population, graph, costs, selection_size)
        
        while len(new_population) < population_size:
            parent1, parent2 = random.sample(new_population, 2)
            child = crossover(parent1, parent2)
            if random.random() < mutation_rate:
                mutate(child)
            new_population.append(child)
            
        population = new_population
        
    best_cycle = min(population, key=lambda cycle: calculate_cycle_length(cycle, graph, costs))
    return best_cycle, calculate_cycle_length(best_cycle, graph, costs)