from solution import *

def test_example_1():
    assert generate(5) == [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]], "Test case 5 rows failed"

def test_example_2():
    assert generate(1) == [[1]], "Test case 1 row failed"

def test_case_num_rows_2():
    assert generate(2) == [[1], [1,1]], "Test case 2 rows failed"

def test_case_num_rows_3():
    assert generate(3) == [[1], [1,1], [1,2,1]], "Test case 3 rows failed"