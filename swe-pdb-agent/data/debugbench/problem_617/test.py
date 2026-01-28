from solution import *

def test_example_1():
    assert maxNiceDivisors(5) == 6, "Example 1 failed"

def test_example_2():
    assert maxNiceDivisors(8) == 18, "Example 2 failed"

def test_case_primefactors_9():
    assert maxNiceDivisors(9) == 27, "Test case for primeFactors=9 failed"

def test_case_primefactors_11():
    assert maxNiceDivisors(11) == 54, "Test case for primeFactors=11 failed"

def test_edge_case_3():
    assert maxNiceDivisors(3) == 3, "Edge case primeFactors=3 failed"