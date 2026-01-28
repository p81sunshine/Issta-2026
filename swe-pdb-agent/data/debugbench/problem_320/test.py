from solution import *

def test_example_1():
    assert validArrangement([[5,1],[4,5],[11,9],[9,4]]) == [[11,9],[9,4],[4,5],[5,1]], "Failed for first example"

def test_example_2():
    result = validArrangement([[1,3],[3,2],[2,1]])
    assert result in ( [[1,3],[3,2],[2,1]], [[2,1],[1,3],[3,2]], [[3,2],[2,1],[1,3]] ), "Failed for second example"

def test_example_3():
    assert validArrangement([[1,2],[1,3],[2,1]]) == [[1,2],[2,1],[1,3]], "Failed for third example"