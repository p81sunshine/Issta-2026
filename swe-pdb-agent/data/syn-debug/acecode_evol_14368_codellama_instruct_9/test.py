import pytest
from acecode_evol_14368_codellama_instruct_9_code import search

def test_case_0():
    assert search([9, 12, -1, 0, 3, 5], 9) == 0

def test_case_1():
    assert search([3, 5, 9, 12, -1, 0], 2) == -1

def test_case_2():
    assert search([1, 3], 3) == 1

def test_case_3():
    assert search([4, 5, 6, 7, 0, 1, 2], 0) == 4

def test_case_4():
    assert search([4, 5, 6, 7, 0, 1, 2], 3) == -1

def test_case_5():
    assert search([1], 1) == 0

def test_case_6():
    assert search([2, 3, 4, 5, 1], 1) == 4

def test_case_7():
    assert search([5, 1, 2, 3, 4], 5) == 0

def test_case_8():
    assert search([3, 4, 5, 1, 2], 4) == 1

def test_case_9():
    assert search([7, 0, 1, 2, 3, 4, 5, 6], 6) == 7

def test_case_10():
    assert search([8, 9, 10, 11, 12, 1, 2, 3], 10) == 2

def test_case_11():
    assert search([6, 7, 8, 9, 10, 3, 4, 5], 3) == 5

def test_case_12():
    assert search([12, 13, 14, 15, 16, 1, 2], 15) == 3

def test_case_13():
    assert search([2, 3, 4, 5, 6, 7, 1], 7) == 5

def test_case_14():
    assert search([1, 2, 3, 4, 5, 6, 7], 0) == -1

def test_case_15():
    assert search([10, 20, 30, 40, 50, 60, 70, 5], 5) == 7

def test_case_16():
    assert search([5, 10, 15, 20, 25, 30, 35], 25) == 4

def test_case_17():
    assert search([3, 4, 5, 1, 2], 5) == 2

def test_case_18():
    assert search([1, 2, 3, 4, 5], 6) == -1