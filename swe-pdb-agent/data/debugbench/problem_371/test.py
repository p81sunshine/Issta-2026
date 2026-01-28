from solution import *

def test_example_1():
    assert max_nice_divisors(5) == 6, "Example 1 failed"

def test_example_2():
    assert max_nice_divisors(8) == 18, "Example 2 failed"

def test_case_primefactors_9():
    assert max_nice_divisors(9) == 27, "Test for primeFactors=9 failed"

def test_edge_case_1():
    assert max_nice_divisors(1) == 1, "Edge case 1 failed"

def test_edge_case_2():
    assert max_nice_divisors(2) == 2, "Edge case 2 failed"

def test_edge_case_3():
    assert max_nice_divisors(3) == 3, "Edge case 3 failed"