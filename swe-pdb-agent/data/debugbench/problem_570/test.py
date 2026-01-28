from solution import *

def test_example_1():
    assert countSubgraphsForEachDiameter(4, [[1,2],[2,3],[2,4]]) == [3,4,0], "Failed for example 1"

def test_example_2():
    assert countSubgraphsForEachDiameter(2, [[1,2]]) == [1], "Failed for example 2"

def test_example_3():
    assert countSubgraphsForEachDiameter(3, [[1,2],[2,3]]) == [2,1], "Failed for example 3"

def test_star_structure_3_nodes():
    assert countSubgraphsForEachDiameter(3, [[1,2],[1,3]]) == [2,1], "Failed for star-shaped 3-node tree"