from solution import *

import math

from solution import *

import math

from solution import *

import math

from solution import genetic_algorithm

def test_genetic_algorithm_quadratic():
    f = lambda x: -(x**2) + 4*x + 1
    bounds = [-10, 10]
    pop_size = 50
    mut_rate = 0.1
    generations = 100
    
    best, best_eval = genetic_algorithm(f, bounds, pop_size, mut_rate, generations)
    
    # The function has a maximum at x = 2, f(2) = 5
    assert best_eval > 4.5
    assert 1.5 < best < 2.5

def test_genetic_algorithm_sine():
    f = lambda x: np.sin(3*x) / x if x != 0 else 0
    bounds = [0.1, 10]
    pop_size = 50
    mut_rate = 0.1
    generations = 100
    
    best, best_eval = genetic_algorithm(f, bounds, pop_size, mut_rate, generations)
    
    # The function will have multiple local maxima, checking if it finds a relatively high value
    assert best_eval > 0.5