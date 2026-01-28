import pytest
from acecode_evol_1086_llama3_1_instruct_47_code import calculator

def test_case_0():
    assert calculator([1, 2, 3], 'addition') == 6

def test_case_1():
    assert calculator([10, 5, 2], 'subtraction') == 3

def test_case_2():
    assert calculator([2, 3, 4], 'multiplication') == 24

def test_case_3():
    assert calculator([100, 5, 2], 'division') == 10.0

def test_case_4():
    assert calculator([1, 2, '3'], 'addition') == None

def test_case_5():
    assert calculator([10, 5, 'a'], 'subtraction') == None

def test_case_6():
    assert calculator([2, 3, 4], 'unknown') == None

def test_case_7():
    assert calculator([2, 0], 'division') == None

def test_case_8():
    assert calculator([10, 2], 'division') == 5.0

def test_case_9():
    assert calculator([], 'addition') == 0

def test_case_10():
    assert calculator([], 'multiplication') == 1

def test_case_11():
    assert calculator([5], 'addition') == 5

def test_case_12():
    assert calculator([5], 'subtraction') == 5

def test_case_13():
    assert calculator([5], 'multiplication') == 5

def test_case_14():
    assert calculator([5], 'division') == 5

def test_case_15():
    assert calculator([10, 0, 5], 'division') == None

def test_case_16():
    assert calculator([1.5, 2.5], 'addition') == 4.0

def test_case_17():
    assert calculator([-1, -2, -3], 'addition') == -6

def test_case_18():
    assert calculator([1, -1, 1], 'addition') == 1

def test_case_19():
    assert calculator([1, 2, 3], 'multiplication') == 6

def test_case_20():
    assert calculator([1, 2, 3], 'subtraction') == -4