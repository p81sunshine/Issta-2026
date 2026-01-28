from solution import *

def test_example_1():
    assert validArrangement([[5,1],[4,5],[11,9],[9,4]]) == [[11,9],[9,4],[4,5],[5,1]]

def test_example_2():
    result = validArrangement([[1,3],[3,2],[2,1]])
    expected_perms = [
        [[1,3],[3,2],[2,1]],
        [[2,1],[1,3],[3,2]],
        [[3,2],[2,1],[1,3]]
    ]
    assert any(result == perm for perm in expected_perms), f"Result {result} is not a valid permutation"

def test_example_3():
    assert validArrangement([[1,2],[1,3],[2,1]]) == [[1,2],[2,1],[1,3]]

def test_cycle_with_start():
    pairs = [[0,1],[1,0],[0,2]]
    assert validArrangement(pairs) == [[0,1],[1,0],[0,2]]