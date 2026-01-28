from solution import *

def test_example_1():
    player1 = [4,10,7,9]
    player2 = [6,5,2,3]
    assert isWinner(player1, player2) == 1, "Example 1 should return 1"

def test_example_2():
    player1 = [3,5,7,6]
    player2 = [8,10,10,2]
    assert isWinner(player1, player2) == 2, "Example 2 should return 2"

def test_example_3():
    player1 = [2,3]
    player2 = [4,1]
    assert isWinner(player1, player2) == 0, "Example 3 should return 0"

def test_buggy_index_logic():
    player1 = [10,5,3]
    player2 = [25]
    assert isWinner(player1, player2) == 1, "Should detect correct bonus calculation for index-2 bonus"