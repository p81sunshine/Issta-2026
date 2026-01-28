from solution import *

def test_example_1():
    assert generate(5) == [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]], "Failed for numRows=5"

def test_example_2():
    assert generate(1) == [[1]], "Failed for numRows=1"

def test_num_rows_2():
    assert generate(2) == [[1], [1,1]], "Failed for numRows=2"

def test_num_rows_3():
    assert generate(3) == [[1], [1,1], [1,2,1]], "Failed for numRows=3"