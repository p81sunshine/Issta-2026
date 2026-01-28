from solution import *
import pytest

def test_initialization_and_single_call():
    sol = create_solution(1.0, 0.0, 0.0)
    point = sol()
    assert isinstance(point, list), "Should return a list"
    assert len(point) == 2, "Should have two coordinates"

def test_multiple_points_in_circle():
    radius = 1.0
    x_center = 0.0
    y_center = 0.0
    sol = create_solution(radius, x_center, y_center)
    for _ in range(100):
        x_val, y_val = sol()
        distance_sq = (x_val - x_center)**2 + (y_val - y_center)**2
        assert distance_sq <= radius**2 + 1e-6, "Point outside circle"

def test_zero_radius():
    radius = 0.0
    x_center = 5.5
    y_center = 3.3
    sol = create_solution(radius, x_center, y_center)
    point = sol()
    assert abs(point[0] - x_center) < 1e-9, "X coordinate should be center"
    assert abs(point[1] - y_center) < 1e-9, "Y coordinate should be center"

def test_non_zero_center():
    radius = 2.0
    x_center = 3.0
    y_center = 4.0
    sol = create_solution(radius, x_center, y_center)
    for _ in range(100):
        x_val, y_val = sol()
        distance_sq = (x_val - x_center)**2 + (y_val - y_center)**2
        assert distance_sq <= radius**2 + 1e-6, "Point outside circle"