from solution import *

def test_example_1():
    actual = generate_pascals_triangle(5)
    expected = [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
    assert actual == expected, "Failed for input 5"

def test_example_2():
    actual = generate_pascals_triangle(1)
    expected = [[1]]
    assert actual == expected, "Failed for input 1"

def test_numrows_2():
    actual = generate_pascals_triangle(2)
    expected = [[1], [1,1]]
    assert actual == expected, "Failed for input 2"

def test_numrows_3():
    actual = generate_pascals_triangle(3)
    expected = [[1], [1,1], [1,2,1]]
    assert actual == expected, "Failed for input 3"