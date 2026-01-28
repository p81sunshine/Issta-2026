from solution import *

def test_example_1():
    assert maxPerformance(6, [2,10,3,1,5,8], [5,4,3,9,7,2], 2) == 60

def test_example_2():
    assert maxPerformance(6, [2,10,3,1,5,8], [5,4,3,9,7,2], 3) == 68

def test_example_3():
    assert maxPerformance(6, [2,10,3,1,5,8], [5,4,3,9,7,2], 4) == 72

def test_edge_case_k_equals_n():
    assert maxPerformance(3, [2,3,1], [5,5,5], 3) == 30

def test_edge_case_single_high_efficiency():
    assert maxPerformance(2, [10, 20], [100, 1], 2) == 1000