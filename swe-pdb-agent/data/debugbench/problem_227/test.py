from solution import *

def test_example_1():
    assert longestCycle([3,3,4,2,3]) == 3, "Failed on example 1"

def test_example_2():
    assert longestCycle([2,-1,3,1]) == -1, "Failed on example 2"

def test_self_loop():
    assert longestCycle([0]) == 1, "Failed on self-loop case"

def test_two_node_cycle():
    assert longestCycle([1,0]) == 2, "Failed on 2-node cycle"

def test_cycle_in_middle():
    assert longestCycle([2,2,3,1]) == 3, "Failed on nested cycle"