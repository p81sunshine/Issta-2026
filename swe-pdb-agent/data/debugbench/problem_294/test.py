from solution import *

def test_example_1():
    pairs = [[5,1],[4,5],[11,9],[9,4]]
    result = valid_arrangement(pairs)
    expected_pairs = set(tuple(p) for p in pairs)
    assert len(result) == len(pairs), "Length mismatch"
    for i in range(len(result) - 1):
        assert result[i][1] == result[i+1][0], f"Invalid sequence at index {i}"
    result_set = set(tuple(p) for p in result)
    assert result_set == expected_pairs, "Missing pairs"

def test_example_2():
    pairs = [[1,3],[3,2],[2,1]]
    result = valid_arrangement(pairs)
    expected_pairs = set(tuple(p) for p in pairs)
    assert len(result) == len(pairs), "Length mismatch"
    for i in range(len(result) - 1):
        assert result[i][1] == result[i+1][0], f"Invalid sequence at index {i}"
    result_set = set(tuple(p) for p in result)
    assert result_set == expected_pairs, "Missing pairs"

def test_example_3():
    pairs = [[1,2],[1,3],[2,1]]
    result = valid_arrangement(pairs)
    expected_pairs = set(tuple(p) for p in pairs)
    assert len(result) == len(pairs), "Length mismatch"
    for i in range(len(result) - 1):
        assert result[i][1] == result[i+1][0], f"Invalid sequence at index {i}"
    result_set = set(tuple(p) for p in result)
    assert result_set == expected_pairs, "Missing pairs"

def test_single_edge_case():
    pairs = [[1,2]]
    result = valid_arrangement(pairs)
    assert len(result) == 1, "Length mismatch"
    assert result[0] == [1,2], "Invalid single edge case"

def test_disconnected_nodes():
    pairs = [[1,2], [3,4], [2,3], [4,5]]
    result = valid_arrangement(pairs)
    expected_pairs = set(tuple(p) for p in pairs)
    assert len(result) == len(pairs), "Length mismatch"
    for i in range(len(result) - 1):
        assert result[i][1] == result[i+1][0], f"Invalid sequence at index {i}"
    result_set = set(tuple(p) for p in result)
    assert result_set == expected_pairs, "Missing pairs"