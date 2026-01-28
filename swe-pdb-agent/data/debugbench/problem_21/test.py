from solution import *

def test_example_1():
    n = 2
    result = getNoZeroIntegers(n)
    assert sum(result) == n, f"Sum of {result} should be {n}"
    assert all('0' not in str(num) for num in result), "Result contains zero"

def test_example_2():
    n = 11
    result = getNoZeroIntegers(n)
    assert sum(result) == n, f"Sum of {result} should be {n}"
    assert all('0' not in str(num) for num in result), "Result contains zero"

def test_edge_case_10():
    n = 10
    result = getNoZeroIntegers(n)
    assert sum(result) == n, f"Sum of {result} should be {n}"
    assert all('0' not in str(num) for num in result), "Result contains zero"

def test_edge_case_100():
    n = 100
    result = getNoZeroIntegers(n)
    assert sum(result) == n, f"Sum of {result} should be {n}"
    assert all('0' not in str(num) for num in result), "Result contains zero"

def test_edge_case_101():
    n = 101
    result = getNoZeroIntegers(n)
    assert sum(result) == n, f"Sum of {result} should be {n}"
    assert all('0' not in str(num) for num in result), "Result contains zero"