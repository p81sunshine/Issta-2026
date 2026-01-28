from solution import *
import random

def test_creation():
    create_rand_point(1.0, 0.0, 0.0)  # Should not raise any error

def test_rand_point_valid():
    radius = 1.0
    x_center = 0.0
    y_center = 0.0
    rand_func = create_rand_point(radius, x_center, y_center)
    for _ in range(100):
        x, y = rand_func()
        distance_sq = (x - x_center)**2 + (y - y_center)**2
        assert distance_sq <= radius**2 + 1e-9, f"Point [{x}, {y}] outside valid circle"

def test_zero_radius():
    radius = 0.0
    x_center = 5.0
    y_center = -3.0
    rand_func = create_rand_point(radius, x_center, y_center)
    for _ in range(10):
        x, y = rand_func()
        assert x == x_center and y == y_center, f"Zero radius case failed: [{x}, {y}] != [{x_center}, {y_center}]"

def test_multiple_points():
    radius = 2.0
    x_center = 1.0
    y_center = 1.0
    rand_func = create_rand_point(radius, x_center, y_center)
    points = [tuple(rand_func()) for _ in range(10)]
    assert len(points) == 10, "Function failed to return multiple points"