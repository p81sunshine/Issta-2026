from solution import *

def test_example_1():
    pairs = [[5,1],[4,5],[11,9],[9,4]]
    result = valid_arrangement(pairs)
    assert len(result) == len(pairs), "Output length mismatch"
    for i in range(1, len(result)):
        assert result[i-1][1] == result[i][0], "Consecutive pairs do not connect"
    assert sorted(result) == sorted(pairs), "Output is not a permutation of input pairs"

def test_example_2():
    pairs = [[1,3],[3,2],[2,1]]
    result = valid_arrangement(pairs)
    assert len(result) == len(pairs), "Output length mismatch"
    for i in range(1, len(result)):
        assert result[i-1][1] == result[i][0], "Consecutive pairs do not connect"
    assert sorted(result) == sorted(pairs), "Output is not a permutation of input pairs"

def test_example_3():
    pairs = [[1,2],[1,3],[2,1]]
    result = valid_arrangement(pairs)
    assert len(result) == len(pairs), "Output length mismatch"
    for i in range(1, len(result)):
        assert result[i-1][1] == result[i][0], "Consecutive pairs do not connect"
    assert sorted(result) == sorted(pairs), "Output is not a permutation of input pairs"

def test_single_pair():
    pairs = [[1,2]]
    result = valid_arrangement(pairs)
    assert len(result) == 1, "Output length mismatch"
    assert result[0] == [1,2], "Incorrect pair arrangement"

def test_two_pair_cycle():
    pairs = [[1,2],[2,1]]
    result = valid_arrangement(pairs)
    assert len(result) == 2, "Output length mismatch"
    assert result[0][1] == result[1][0], "Consecutive pairs do not connect"
    assert sorted(result) == sorted(pairs), "Output is not a permutation of input pairs"