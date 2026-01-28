from solution import *

def test_example_1():
    pairs = [[5,1],[4,5],[11,9],[9,4]]
    expected = [[11,9],[9,4],[4,5],[5,1]]
    assert validArrangement(pairs) == expected

def test_example_3():
    pairs = [[1,2],[1,3],[2,1]]
    expected = [[1,2],[2,1],[1,3]]
    assert validArrangement(pairs) == expected

def test_single_edge():
    pairs = [[1,2]]
    expected = [[1,2]]
    assert validArrangement(pairs) == expected

def test_custom_case():
    pairs = [[0,1],[1,2],[2,0],[0,3]]
    expected = [[0,1],[1,2],[2,0],[0,3]]
    result = validArrangement(pairs)
    # All valid arrangements are acceptable as long as consecutive pairs connect
    assert all(result[i][1] == result[i+1][0] for i in range(len(result)-1)), "Consecutive pairs do not connect"
    assert set(map(tuple, result)) == set((x, y) for x, y in pairs), "Not all edges used"