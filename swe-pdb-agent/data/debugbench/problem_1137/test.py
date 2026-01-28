from solution import *

def test_example_1():
    n = 4
    left = [4, 3]
    right = [0, 1]
    expected = 4
    actual = get_last_moment(n, left, right)
    assert actual == expected, f"Expected {expected} but got {actual}"

def test_example_2():
    n = 7
    left = []
    right = [0, 1, 2, 3, 4, 5, 6, 7]
    expected = 7
    actual = get_last_moment(n, left, right)
    assert actual == expected, f"Expected {expected} but got {actual}"

def test_example_3():
    n = 7
    left = [0, 1, 2, 3, 4, 5, 6, 7]
    right = []
    expected = 7
    actual = get_last_moment(n, left, right)
    assert actual == expected, f"Expected {expected} but got {actual}"

def test_both_empty():
    n = 5
    left = []
    right = []
    expected = 0
    actual = get_last_moment(n, left, right)
    assert actual == expected, f"Expected {expected} but got {actual}"

def test_mixed_case():
    n = 5
    left = [2, 3]
    right = [1, 2]
    expected = 4  # max(3, 5 - 1) = 4
    actual = get_last_moment(n, left, right)
    assert actual == expected, f"Expected {expected} but got {actual}"