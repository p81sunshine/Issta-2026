from solution import *

def test_example_1():
    assert canFinish(2, [[1,0]]) is True, "Example 1 failed"

def test_example_2():
    assert canFinish(2, [[1,0],[0,1]]) is False, "Example 2 failed"

def test_no_prerequisites():
    assert canFinish(3, []) is True, "No prerequisites case failed"

def test_chain_prerequisites():
    assert canFinish(3, [[1,0], [2,1]]) is True, "Chain of prerequisites failed"

def test_complex_cycle():
    assert canFinish(4, [[1,0],[2,1],[3,2],[3,1],[0,3]]) is False, "Complex cycle detection failed"