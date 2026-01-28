from solution import *
import math

def test_all():
    assert binary_search([1, 2, 3, 4, 5], 3) == 2
    assert binary_search([1, 2, 3, 4, 5], 6) == -1
    assert binary_search([1, 2, 3, 3, 4], 3) == 2
    assert binary_search([1], 1) == 0
    assert binary_search([1], 0) == -1
    assert binary_search([], 1) == -1
    assert binary_search([0, 1, 3, 3, 4, 5, 6], 3) == 2
    assert binary_search([3, 3, 3, 4, 5], 3) == 0
    assert binary_search([1, 2, 4, 5, 6, 6, 6], 6) == 4
    assert binary_search([1, 2, 3, 3, 3, 4, 5], 3) == 2
    assert binary_search([2, 2, 2, 2, 2], 2) == 0
    assert binary_search([2, 2, 2, 2, 2], 3) == -1
    assert binary_search(list(range(10000)), 5000) == 5000
    assert binary_search([-5, -4, -3, -2, -1], -3) == 2 
    assert binary_search([-3, -2, -1, 0, 1, 2, 3], 0) == 3 
    assert binary_search([2, 2, 2, 3, 4, 5, 6], 2) == 0 
    assert binary_search([1, 1, 2, 2, 2, 3, 4], 2) == 2 
    assert binary_search([1] * 1000 + [2] * 1000 + [3] * 1000, 2) == 1000
    assert binary_search([1, 2, 2, 2, 3, 4, 5], 2) == 1