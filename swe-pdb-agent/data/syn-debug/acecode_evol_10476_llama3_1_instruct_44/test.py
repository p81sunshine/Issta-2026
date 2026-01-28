import pytest
from acecode_evol_10476_llama3_1_instruct_44_code import findMissingRanges, getRange

def test_case_0():
    assert findMissingRanges([0,1,3,50,75], 0, 99) == ['2', '4->49', '51->74', '76->99']

def test_case_1():
    assert findMissingRanges([], 1, 1) == ['1']

def test_case_2():
    assert findMissingRanges([], -3, -1) == ['-3->-1']

def test_case_3():
    assert findMissingRanges([-1], -1, -1) == []

def test_case_4():
    assert findMissingRanges([-1], -2, -1) == ['-2']

def test_case_5():
    assert findMissingRanges([1, 2, 3], 0, 5) == ['0', '4->5']

def test_case_6():
    assert findMissingRanges([2, 3, 5], 0, 5) == ['0->1', '4']

def test_case_7():
    assert findMissingRanges([-10, -5, 0, 3], -10, 3) == ['-9->-6', '-4->-1', '1->2']

def test_case_8():
    assert findMissingRanges([], 10, 20) == ['10->20']

def test_case_9():
    assert findMissingRanges([5, 6, 7], 0, 10) == ['0->4', '8->10']

def test_case_10():
    assert findMissingRanges([1, 2, 3, 4], 0, 5) == ['0', '5']

def test_case_11():
    assert findMissingRanges([-5, 0, 1], -5, 1) == ['-4->-1']

def test_case_12():
    assert findMissingRanges([0], 0, 1) == ['1']

def test_case_13():
    assert findMissingRanges([], -5, -3) == ['-5->-3']

def test_case_14():
    assert findMissingRanges([4, 5, 6, 7], 0, 10) == ['0->3', '8->10']

def test_case_15():
    assert findMissingRanges([0, 1, 2], 0, 5) == ['3->5']

def test_case_16():
    assert findMissingRanges([1, 3, 4, 5], 1, 6) == ['2', '6']

def test_case_17():
    assert findMissingRanges([8, 9, 10], 5, 15) == ['5->7', '11->15']

def test_case_18():
    assert findMissingRanges([2, 4, 6, 8], 1, 9) == ['1', '3', '5', '7', '9']