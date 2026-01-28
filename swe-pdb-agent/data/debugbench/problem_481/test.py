from solution import *

def test_example_1():
    input_nums = [5, 2, 3, 1]
    expected = [1, 2, 3, 5]
    assert sortArray(input_nums) == expected, "Failed for example 1"

def test_example_2():
    input_nums = [5, 1, 1, 2, 0, 0]
    expected = [0, 0, 1, 1, 2, 5]
    assert sortArray(input_nums) == expected, "Failed for example 2"

def test_edge_case_empty():
    input_nums = []
    expected = []
    assert sortArray(input_nums) == expected, "Failed for empty list"

def test_edge_case_single_element():
    input_nums = [3]
    expected = [3]
    assert sortArray(input_nums) == expected, "Failed for single element"