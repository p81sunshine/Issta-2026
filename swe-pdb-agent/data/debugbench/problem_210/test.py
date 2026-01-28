from solution import *

def test_example_1():
    assert countSubgraphsForEachDiameter(4, [[1,2],[2,3],[2,4]]) == [3,4,0], "Test case 1 failed"

def test_example_2():
    assert countSubgraphsForEachDiameter(2, [[1,2]]) == [1], "Test case 2 failed"

def test_example_3():
    assert countSubgraphsForEachDiameter(3, [[1,2],[2,3]]) == [2,1], "Test case 3 failed"

def test_small_chain():
    # Test a 3-node chain with different edge ordering
    assert countSubgraphsForEachDiameter(3, [[1,3],[2,3]]) == [2,1], "Small chain test failed"