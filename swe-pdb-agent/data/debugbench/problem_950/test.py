from solution import *

def test_example_1():
    radius = 1.0
    x_center = 0.0
    y_center = 0.0
    func = create_rand_point(radius, x_center, y_center)
    for _ in range(3):
        x, y = func()
        distance_sq = (x - x_center)**2 + (y - y_center)**2
        assert distance_sq <= radius**2 + 1e-6, f"Point [{x}, {y}] is outside the circle"

def test_zero_radius():
    radius = 0.0
    x_center = 5.0
    y_center = 5.0
    func = create_rand_point(radius, x_center, y_center)
    expected = [x_center, y_center]
    for _ in range(5):
        point = func()
        assert point[0] == expected[0] and point[1] == expected[1], f"Expected {expected} but got {point}"

def test_multiple_centers():
    radius = 2.0
    x_center = 3.0
    y_center = 4.0
    func = create_rand_point(radius, x_center, y_center)
    for _ in range(5):
        x, y = func()
        distance_sq = (x - x_center)**2 + (y - y_center)**2
        assert distance_sq <= radius**2 + 1e-6, f"Point [{x}, {y}] is outside the circle"

def test_randomness():
    radius = 1.0
    x_center = 0.0
    y_center = 0.0
    func = create_rand_point(radius, x_center, y_center)
    points = {tuple(func()) for _ in range(100)}
    assert len(points) > 1, "All points are identical, randomness might be broken"