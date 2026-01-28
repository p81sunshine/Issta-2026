from solution import *
import math

# checking that nothing that shouldn't change has changed

def test_all():
    cities = generate_cities(10)

    assert cities == [City(2, 7), City(7, 2), City(6, 5), City(6, 8), City(1, 8), City(1, 1), City(7, 4), City(0, 10), City(10, 3), City(5, 3)]

    assert distance(cities[0], cities[1]) == distance(cities[1], cities[0])
    assert distance(cities[0], City(2, 0)) == 7
    assert distance(cities[9], City(8, 7)) == 5

    population = generate_population(cities, 5)
    assert population[1] == [City(x, y) for x, y in [(7, 4), (0, 10), (1, 8), (5, 3), (6, 8), (7, 2), (2, 7), (1, 1), (6, 5), (10, 3)]]
    assert population[4] == [City(x, y) for x, y in [(10, 3), (1, 1), (0, 10), (6, 8), (2, 7), (5, 3), (6, 5), (7, 4), (7, 2), (1, 8)]]

    p1 = tournament_selection(population)
    p2 = tournament_selection(population)

    assert p1 == [City(x, y) for x, y in [(7, 4), (0, 10), (1, 8), (5, 3), (6, 8), (7, 2), (2, 7), (1, 1), (6, 5), (10, 3)]]
    assert p2 == [City(x, y) for x, y in [(1, 8), (6, 8), (6, 5), (7, 2), (7, 4), (0, 10), (5, 3), (10, 3), (1, 1), (2, 7)]]

    afterpop1 = [City(x, y) for x, y in [(7, 4), (0, 10), (1, 8), (5, 3), (6, 8), (10, 3), (2, 7), (1, 1), (6, 5), (7, 2)]]
    assert mutate(population[1]) == afterpop1

    afterp2 = [City(x, y) for x, y in [(1, 8), (6, 8), (6, 5), (7, 2), (7, 4), (0, 10), (5, 3), (10, 3), (1, 1), (2, 7)]]
    assert mutate(p2) == afterp2

    afterp1 = [City(x, y) for x, y in [(10, 3), (1, 1), (0, 10), (6, 8), (2, 7), (5, 3), (6, 5), (7, 4), (7, 2), (1, 8)]]
    assert mutate(population[4]) == afterp1

    assert get_crossing_point(p1) == 2
    assert get_crossing_point(afterp1) == 1

    # checking crossover and next_generation, check no repeat cities in children

    next_gen = next_generation(population, 0.8, 0.2)
    city_set = set(cities)

    for individual in next_gen:
        assert set(individual) == city_set

    city = City(1, 1)
    assert city == City(1, 1)
    assert city != City(1, 2)
    assert city != City(2, 1)
    assert city != 4