from solution import *

import math

from solution import *

import math

from solution import *

import math

def test_calculate_cycle_length():
    graph = [[(1, 10), (2, 15)], [(0, 10), (2, 10)], [(0, 15), (1, 10)]]
    costs = [1, 2, 3]
    cycle = [0, 1, 2]
    
    length = calculate_cycle_length(cycle, graph, costs)
    assert length == 1 + 2 + 3 + 10 + 10 + 15

def test_create_initial_population():
    graph = [[(1, 10), (2, 15)], [(0, 10), (2, 10)], [(0, 15), (1, 10)]]
    population = create_initial_population(graph, 5)
    
    assert len(population) == 5
    for cycle in population:
        assert sorted(cycle) == [0, 1, 2]

def test_select_best_population():
    graph = [[(1, 10), (2, 15)], [(0, 10), (2, 10)], [(0, 15), (1, 10)]]
    costs = [1, 2, 3]
    population = [[0, 1, 2], [2, 0, 1], [1, 2, 0], [0, 2, 1], [1, 0, 2]]
    
    selected_population = select_best_population(population, graph, costs, 2)
    assert len(selected_population) == 2

def test_crossover():
    parent1 = [0, 1, 2, 3, 4]
    parent2 = [3, 2, 1, 0, 4]
    
    child = crossover(parent1, parent2)
    
    assert len(child) == len(parent1)
    assert sorted(child) == sorted(parent1)

def test_mutate():
    cycle = [0, 1, 2, 3, 4]
    mutate(cycle)
    
    assert len(cycle) == 5
    assert sorted(cycle) == [0, 1, 2, 3, 4]

def test_genetic_algorithm():
    graph = [[(1, 10), (2, 15)], [(0, 10), (2, 10)], [(0, 15), (1, 10)]]
    costs = [1, 2, 3]
    
    best_cycle, best_length = genetic_algorithm(graph, costs, population_size=10, generations=50, mutation_rate=0.1, selection_size=5)
    
    assert len(best_cycle) == len(graph)
    assert best_length > 0