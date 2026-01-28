import random
import numpy as np

def genetic_algorithm(f, bounds, pop_size, mut_rate, generations):
    def init_population(bounds, pop_size):
        return [random.uniform(bounds[0], bounds[1]) for _ in range(pop_size)]

    def selection(pop, scores, k=3):
        # Binary tournament selection
        selection_ix = np.random.randint(len(pop))
        for ix in np.random.randint(0, len(pop), k-1):
            if scores[ix] > scores[selection_ix]:
                selection_ix = ix
        return pop[selection_ix]
    
    def crossover(p1, p2, r_cross):
        # point of crossover
        if random.random() < r_cross:
            return (p1 + p2) / 2.0
        else:
            return p1

    def mutation(c, bounds, r_mut):
        if random.random() < r_mut:
            c += random.uniform(-1, 1) * (bounds[1] - bounds[0]) * 0.1
        # Ensure bounds are maintained
        c = max(bounds[0], min(bounds[1], c))
        return c

    # initial population
    pop = init_population(bounds, pop_size)
    # keep track of best solution
    best, best_eval = 0, f(pop[0])

    # iterate through generations
    for gen in range(generations):
        # evaluate all candidates in the population
        scores = [f(c) for c in pop]
        # check for new best solution
        for i in range(pop_size):
            if scores[i] > best_eval:
                best, best_eval = pop[i], scores[i]

        # select parents
        selected = [selection(pop, scores) for _ in range(pop_size // 2)]
        
        # create the next generation
        children = list()
        for i in range(0, pop_size, 2):
            p1, p2 = selected[i], selected[i+1]
            # crossover and mutation
            for c in [crossover(p1, p2, 0.9), crossover(p1, p2, 0.9)]:
                c = mutation(c, bounds, mut_rate)
                children.append(c)
        # replace population with children
        pop = children
    return [best, best_eval]