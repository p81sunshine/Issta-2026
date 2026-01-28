from solution import *

def test_example_1():
    pairs = [[5,1],[4,5],[11,9],[9,4]]
    expected = [[11,9],[9,4],[4,5],[5,1]]
    assert validArrangement(pairs) == expected, "Failed example 1"

def test_example_2():
    pairs = [[1,3],[3,2],[2,1]]
    actual = validArrangement(pairs)
    expected_pairs_set = set(map(tuple, pairs))
    actual_pairs_set = set(map(tuple, actual))
    assert len(actual) == len(pairs), "Length mismatch in example 2"
    assert actual_pairs_set == expected_pairs_set, f"Expected pairs {expected_pairs_set}, got {actual_pairs_set}"
    for i in range(len(actual) - 1):
        assert actual[i][1] == actual[i+1][0], f"Invalid sequence in example 2 at i={i}"

def test_example_3():
    pairs = [[1,2],[1,3],[2,1]]
    expected = [[1,2],[2,1],[1,3]]
    assert validArrangement(pairs) == expected, "Failed example 3"

def test_cycle_with_multiple_edges():
    pairs = [[1,2],[2,3],[3,4],[4,1]]
    actual = validArrangement(pairs)
    expected_pairs_set = set(map(tuple, pairs))
    actual_pairs_set = set(map(tuple, actual))
    assert len(actual) == len(pairs), "Length mismatch in cycle test"
    assert actual_pairs_set == expected_pairs_set, "Missing pairs in cycle test"
    for i in range(len(actual) - 1):
        assert actual[i][1] == actual[i+1][0], f"Invalid sequence in cycle test at i={i}"