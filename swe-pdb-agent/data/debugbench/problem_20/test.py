from solution import *
import random

def test_example_1():
    x, y, r = create_solution(1.0, 0.0, 0.0)
    for _ in range(3):
        point = rand_point(x, y, r)
        distance_sq = (point[0] - 0.0)**2 + (point[1] - 0.0)**2
        assert distance_sq <= (1.0 + 1e-9)**2, f"Point {point} is outside the circle"

def test_another_case():
    radius = 2.0
    x_center = 1.5
    y_center = -1.0
    x, y, r = create_solution(radius, x_center, y_center)
    for _ in range(5):
        point = rand_point(x, y, r)
        distance_sq = (point[0] - x_center)**2 + (point[1] - y_center)**2
        assert distance_sq <= (radius + 1e-9)**2, f"Point {point} is outside the circle"

def test_output_format():
    x, y, r = create_solution(0.5, 2.0, 3.0)
    point = rand_point(x, y, r)
    assert len(point) == 2, "Output should be a list of exactly two elements"
    assert all(isinstance(coord, float) for coord in point), "Coordinates should be floats"

def test_edge_case_zero_radius():
    x_center = 100.0
    y_center = -50.0
    x, y, r = create_solution(0.0, x_center, y_center)
    point = rand_point(x, y, r)
    assert point[0] == x_center and point[1] == y_center, "Zero radius should return the center point"