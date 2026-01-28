from solution import *

def test_example_1():
    pairs = [[5,1],[4,5],[11,9],[9,4]]
    expected = [[11,9],[9,4],[4,5],[5,1]]
    assert validArrangement(pairs) == expected, "Failed example 1"

def test_example_2():
    pairs = [[1,3],[3,2],[2,1]]
    actual = validArrangement(pairs)
    # Check all edges are present
    expected_edges = set(tuple(p) for p in pairs)
    actual_edges = set(tuple(p) for p in actual)
    assert actual_edges == expected_edges, "Edges do not match"
    # Check sequence is valid
    for i in range(len(actual)-1):
        assert actual[i][1] == actual[i+1][0], f"Invalid sequence at index {i}"

def test_example_3():
    pairs = [[1,2],[1,3],[2,1]]
    expected = [[1,2],[2,1],[1,3]]
    assert validArrangement(pairs) == expected, "Failed example 3"

def test_single_pair():
    pairs = [[1,2]]
    assert validArrangement(pairs) == [[1,2]], "Failed single pair case"