from solution import *

def test_example_1():
    matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
    expected = [[1,2,10],[4,5,7,8]]
    actual = findWinners(matches)
    assert actual == expected, f"Expected {expected} but got {actual}"

def test_example_2():
    matches = [[2,3],[1,3],[5,4],[6,4]]
    expected = [[1,2,5,6],[]]
    actual = findWinners(matches)
    assert actual == expected, f"Expected {expected} but got {actual}"

def test_single_match():
    matches = [[1,2]]
    expected = [[1], [2]]
    actual = findWinners(matches)
    assert actual == expected, f"Expected {expected} but got {actual}"

def test_two_matches():
    matches = [[1,2], [2,3]]
    expected = [[1], [2,3]]
    actual = findWinners(matches)
    assert actual == expected, f"Expected {expected} but got {actual}"