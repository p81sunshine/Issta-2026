from solution import *

def test_example_1():
    nums = [6,2,2,2,6]
    edges = [[0,1],[1,2],[1,3],[3,4]]
    assert componentValue(nums, edges) == 2, "Example 1 should return 2"

def test_example_2():
    nums = [2]
    edges = []
    assert componentValue(nums, edges) == 0, "Example 2 should return 0"

def test_two_nodes_equal_sum():
    nums = [2,2]
    edges = [[0,1]]
    assert componentValue(nums, edges) == 1, "Two nodes with equal sum should return 1"

def test_no_possible_split():
    nums = [3,1,3]
    edges = [[0,1],[1,2]]
    assert componentValue(nums, edges) == 0, "No possible split should return 0"

def test_single_edge():
    nums = [1,1]
    edges = [[0,1]]
    assert componentValue(nums, edges) == 1, "Split into two components with sum 1 each"