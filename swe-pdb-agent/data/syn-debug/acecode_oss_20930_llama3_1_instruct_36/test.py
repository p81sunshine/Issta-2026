import pytest
from acecode_oss_20930_llama3_1_instruct_36_code import degrees_of_separation

def test_case_0():
    assert degrees_of_separation(1, 2, [(1, 2)]) == 1

def test_case_1():
    assert degrees_of_separation(1, 3, [(1, 2), (2, 3)]) == 2

def test_case_2():
    assert degrees_of_separation(1, 4, [(1, 2), (2, 3)]) == -1

def test_case_3():
    assert degrees_of_separation(1, 1, [(1, 2)]) == 0

def test_case_4():
    assert degrees_of_separation(2, 3, [(1, 2), (2, 3), (3, 4)]) == 1

def test_case_5():
    assert degrees_of_separation(1, 4, [(1, 2), (2, 3), (3, 4)]) == 3

def test_case_6():
    assert degrees_of_separation(5, 6, []) == -1

def test_case_7():
    assert degrees_of_separation(1, 3, [(1, 2), (4, 5)]) == -1

def test_case_8():
    assert degrees_of_separation(1, 5, [(1, 2), (2, 3), (3, 4), (4, 5)]) == 4

def test_case_9():
    assert degrees_of_separation(10, 20, [(10, 15), (15, 20)]) == 2

def test_case_10():
    assert degrees_of_separation(100, 200, [(100, 150), (150, 200), (200, 250)]) == 2

def test_case_11():
    assert degrees_of_separation(1, 10, [(1, 2), (2, 3), (3, 4)]) == -1

def test_case_12():
    assert degrees_of_separation(7, 8, [(7, 9), (9, 8), (8, 10)]) == 2

def test_case_13():
    assert degrees_of_separation(3, 3, [(2, 3), (3, 4)]) == 0

def test_case_14():
    assert degrees_of_separation(4, 5, [(4, 1), (1, 2), (2, 5)]) == 3

def test_case_15():
    assert degrees_of_separation(6, 6, [(1, 2), (2, 3)]) == 0

def test_case_16():
    assert degrees_of_separation(2, 8, [(2, 3), (3, 4), (4, 5), (5, 6), (6, 7)]) == -1

def test_case_17():
    assert degrees_of_separation(8, 9, [(7, 8), (8, 9)]) == 1

def test_case_18():
    assert degrees_of_separation(0, 1, [(0, 2), (1, 3)]) == -1