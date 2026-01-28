from solution import *

def test_example_1():
    pairs = [[5,1],[4,5],[11,9],[9,4]]
    result = validArrangement(pairs)
    assert len(result) == len(pairs), "Result length mismatch"
    for i in range(len(result) - 1):
        assert result[i][1] == result[i+1][0], "Consecutive pairs not connected"
    assert sorted(result) == sorted(pairs), "Result does not contain all input pairs"

def test_example_2():
    pairs = [[1,3],[3,2],[2,1]]
    result = validArrangement(pairs)
    assert len(result) == len(pairs), "Result length mismatch"
    for i in range(len(result) - 1):
        assert result[i][1] == result[i+1][0], "Consecutive pairs not connected"
    assert sorted(result) == sorted(pairs), "Result does not contain all input pairs"

def test_example_3():
    pairs = [[1,2],[1,3],[2,1]]
    result = validArrangement(pairs)
    assert len(result) == len(pairs), "Result length mismatch"
    for i in range(len(result) - 1):
        assert result[i][1] == result[i+1][0], "Consecutive pairs not connected"
    assert sorted(result) == sorted(pairs), "Result does not contain all input pairs"

def test_single_pair():
    pairs = [[1,2]]
    result = validArrangement(pairs)
    assert len(result) == 1, "Result length mismatch"
    assert result[0] == [1,2], "Result does not match input"

def test_cycle_two_pairs():
    pairs = [[1,2],[2,1]]
    result = validArrangement(pairs)
    assert len(result) == 2, "Result length mismatch"
    assert sorted(result) == sorted(pairs), "Result does not contain all input pairs"
    assert result[0][1] == result[1][0] or result[1][1] == result[0][0], "Consecutive pairs not connected"