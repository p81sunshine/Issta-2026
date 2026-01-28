from solution import *

def test_example_1():
    input_val = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
    expected = [[1,2,10],[4,5,7,8]]
    actual = findWinners(input_val)
    assert actual == expected, f"Expected {expected}, but got {actual}"

def test_example_2():
    input_val = [[2,3],[1,3],[5,4],[6,4]]
    expected = [[1,2,5,6],[]]
    actual = findWinners(input_val)
    assert actual == expected, f"Expected {expected}, but got {actual}"

def test_empty_input():
    input_val = []
    expected = [[], []]
    actual = findWinners(input_val)
    assert actual == expected, "Empty input should return two empty lists"

def test_single_match():
    input_val = [[1,2]]
    expected = [[1], [2]]
    actual = findWinners(input_val)
    assert actual == expected, "Single match should have winner in first list and loser in second"

def test_player_with_both_wins_and_losses():
    input_val = [[1,2], [2,3], [3,2]]
    expected = [[1], [3]]
    actual = findWinners(input_val)
    assert actual == expected, "Player 1 has no losses, player 3 has one loss"