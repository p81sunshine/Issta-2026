from solution import *

def test_example_1():
    assert valid_arrangement([[5,1],[4,5],[11,9],[9,4]]) == [[11,9],[9,4],[4,5],[5,1]]

def test_example_2():
    result = valid_arrangement([[1,3],[3,2],[2,1]])
    expected = [[1,3],[3,2],[2,1]]
    assert len(result) == len(expected)
    for i in range(len(result)-1):
        assert result[i][1] == result[i+1][0], f"Invalid sequence at index {i}"

def test_example_3():
    assert valid_arrangement([[1,2],[1,3],[2,1]]) == [[1,2],[2,1],[1,3]]

def test_single_pair():
    assert valid_arrangement([[1,2]]) == [[1,2]]

def test_cycle_with_more_nodes():
    result = valid_arrangement([[1,2],[2,3],[3,1]])
    assert len(result) == 3
    for i in range(len(result)-1):
        assert result[i][1] == result[i+1][0], f"Invalid sequence at index {i}"