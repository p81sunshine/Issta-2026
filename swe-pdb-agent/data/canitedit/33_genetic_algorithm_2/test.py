from solution import *
import math

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

    next_gen = next_generation(population, 0.8, 0.2)
    city_set = set(cities)

    for individual in next_gen:
        assert set(individual) == city_set

    # checking that mutation at 100% chance will always produce a mutation

    mutation_cities = generate_cities(5)
    mutation_test = generate_population(mutation_cities, 1)[0]

    for i in range(10000):
        diff = mutate(mutation_test, 1)
        assert diff != mutation_test

    city = City(1, 1)
    assert city == City(1, 1)
    assert city != City(1, 2)
    assert city != City(2, 1)
    assert city != 4