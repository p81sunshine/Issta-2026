from solution import *

def test_example_1():
    assert jump(nums=[2,3,1,1,4]) == 2, "Example 1 failed"

def test_example_2():
    assert jump(nums=[2,3,0,1,4]) == 2, "Example 2 failed"

def test_edge_case_single_element():
    assert jump(nums=[5]) == 0, "Single element edge case failed"

def test_long_jump_short_array():
    assert jump(nums=[3,1,1,1]) == 1, "Direct jump case failed"

def test_step_by_step():
    assert jump(nums=[1,1,1,1]) == 3, "Sequential jumps case failed"