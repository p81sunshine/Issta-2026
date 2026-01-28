from solution import *

def test_example_1():
    input = [[5,1],[4,5],[11,9],[9,4]]
    output = validArrangement(input)
    expected_pairs = [[5,1],[4,5],[11,9],[9,4]]
    assert sorted(output) == sorted(expected_pairs), "All input pairs must be present"
    for i in range(len(output)-1):
        assert output[i][1] == output[i+1][0], f"Invalid sequence at {i}"

def test_example_3():
    input = [[1,2],[1,3],[2,1]]
    output = validArrangement(input)
    expected_pairs = [[1,2],[1,3],[2,1]]
    assert sorted(output) == sorted(expected_pairs), "All input pairs must be present"
    for i in range(len(output)-1):
        assert output[i][1] == output[i+1][0], f"Invalid sequence at {i}"

def test_single_edge():
    input = [[1,2]]
    output = validArrangement(input)
    assert output == [[1,2]], "Single edge case must return the input"

def test_cycle_of_three():
    input = [[1,2],[2,3],[3,1]]
    output = validArrangement(input)
    expected_pairs = [[1,2],[2,3],[3,1]]
    assert sorted(output) == sorted(expected_pairs), "All input pairs must be present"
    for i in range(len(output)-1):
        assert output[i][1] == output[i+1][0], f"Invalid sequence at {i}"