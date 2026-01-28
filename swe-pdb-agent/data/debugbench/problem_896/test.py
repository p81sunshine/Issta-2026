from solution import *

def test_example_1():
    assert longestCycle([3,3,4,2,3]) == 3, "Failed to detect cycle: 2->4->3->2"

def test_example_2():
    assert longestCycle([2,-1,3,1]) == -1, "No cycles should be found"

def test_self_loop():
    assert longestCycle([0]) == 1, "Self-loop should return 1"

def test_two_cycles():
    assert longestCycle([1,0,3,2]) == 2, "Maximum of two 2-length cycles"

def test_chain_to_cycle():
    assert longestCycle([1,2,3,1]) == 3, "Chain leading to cycle 1->2->3->1"