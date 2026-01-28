from solution import *

def test_example_1():
    deck = [17,13,11,2,3,5,7]
    expected = [2,13,3,11,5,17,7]
    result = deckRevealedIncreasing(deck)
    assert result == expected, f"Example 1 failed: {result} != {expected}"

def test_example_2():
    deck = [1, 1000]
    expected = [1, 1000]
    result = deckRevealedIncreasing(deck)
    assert result == expected, f"Example 2 failed: {result} != {expected}"

def test_single_element():
    deck = [5]
    expected = [5]
    result = deckRevealedIncreasing(deck)
    assert result == expected, f"Single element test failed: {result} != {expected}"

def test_two_elements():
    deck = [2, 1]
    expected = [1, 2]
    result = deckRevealedIncreasing(deck)
    assert result == expected, f"Two elements test failed: {result} != {expected}"

def test_three_elements():
    deck = [3, 1, 2]
    expected = [1, 3, 2]
    result = deckRevealedIncreasing(deck)
    assert result == expected, f"Three elements test failed: {result} != {expected}"