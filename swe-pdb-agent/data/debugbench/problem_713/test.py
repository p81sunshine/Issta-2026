from solution import *

def test_example_1():
    input_pairs = [[5,1],[4,5],[11,9],[9,4]]
    actual = validArrangement(input_pairs)
    for i in range(len(actual)-1):
        assert actual[i][1] == actual[i+1][0], f"Consecutive pairs failed at index {i}"
    assert sorted(actual) == sorted(input_pairs), "Output not a permutation of input"

def test_example_2():
    input_pairs = [[1,3],[3,2],[2,1]]
    actual = validArrangement(input_pairs)
    for i in range(len(actual)-1):
        assert actual[i][1] == actual[i+1][0], f"Consecutive pairs failed at index {i}"
    assert sorted(actual) == sorted(input_pairs), "Output not a permutation of input"

def test_example_3():
    input_pairs = [[1,2],[1,3],[2,1]]
    actual = validArrangement(input_pairs)
    for i in range(len(actual)-1):
        assert actual[i][1] == actual[i+1][0], f"Consecutive pairs failed at index {i}"
    assert sorted(actual) == sorted(input_pairs), "Output not a permutation of input"

def test_single_pair():
    input_pairs = [[1,2]]
    actual = validArrangement(input_pairs)
    assert actual == [[1,2]], "Single pair should return itself"

def test_another_case():
    input_pairs = [[0,1], [1,2], [2,0]]
    actual = validArrangement(input_pairs)
    for i in range(len(actual)-1):
        assert actual[i][1] == actual[i+1][0], f"Consecutive pairs failed at index {i}"
    assert sorted(actual) == sorted(input_pairs), "Output not a permutation of input"