from solution import *
import random

def test_example_1():
    solution = create_solution(1.0, 0.0, 0.0)
    for _ in range(5):
        x_rand, y_rand = solution()
        assert (x_rand - 0.0)**2 + (y_rand - 0.0)**2 <= (1.0 + 1e-9)**2, "Point outside the circle"

def test_edge_case_radius_zero():
    solution = create_solution(0.0, 5.0, 5.0)
    for _ in range(5):
        x_rand, y_rand = solution()
        assert x_rand == 5.0 and y_rand == 5.0, "Expected center point when radius is zero"

def test_different_center_radius():
    solution = create_solution(2.0, 1.0, 2.0)
    for _ in range(5):
        x_rand, y_rand = solution()
        assert (x_rand - 1.0)**2 + (y_rand - 2.0)**2 <= (2.0 + 1e-9)**2, "Point outside the specified circle"

def test_small_radius():
    solution = create_solution(0.1, 0.0, 0.0)
    for _ in range(5):
        x_rand, y_rand = solution()
        assert (x_rand**2 + y_rand**2) <= (0.1 + 1e-9)**2, "Point outside small radius circle"

def test_return_type():
    solution = create_solution(1.0, 0.0, 0.0)
    point = solution()
    assert isinstance(point, list), "Return value should be a list"
    assert len(point) == 2, "Return value should have two elements"
    assert all(isinstance(coord, float) for coord in point), "Coordinates should be floats"