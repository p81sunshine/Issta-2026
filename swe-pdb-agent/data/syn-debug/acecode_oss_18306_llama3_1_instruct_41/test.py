import pytest
from acecode_oss_18306_llama3_1_instruct_41_code import purchase_item

def test_case_0():
    assert purchase_item({'A': (2, 1.5), 'B': (0, 2.0)}, 'A', 2.0) == 'Dispensing A. Change: 0.5'

def test_case_1():
    assert purchase_item({'A': (0, 1.5), 'B': (3, 2.0)}, 'A', 1.5) == 'Item out of stock'

def test_case_2():
    assert purchase_item({'A': (1, 1.5), 'B': (3, 2.0)}, 'B', 1.0) == 'Insufficient funds'

def test_case_3():
    assert purchase_item({'A': (1, 1.5), 'B': (3, 2.0)}, 'B', 2.0) == 'Dispensing B. Change: 0.0'

def test_case_4():
    assert purchase_item({'C': (5, 3.0)}, 'C', 3.0) == 'Dispensing C. Change: 0.0'

def test_case_5():
    assert purchase_item({'C': (5, 3.0)}, 'C', 4.0) == 'Dispensing C. Change: 1.0'

def test_case_6():
    assert purchase_item({'D': (0, 2.0)}, 'D', 2.0) == 'Item out of stock'

def test_case_7():
    assert purchase_item({'E': (1, 1.0)}, 'F', 1.0) == 'Item out of stock'

def test_case_8():
    assert purchase_item({'A': (5, 1.0)}, 'A', 0.5) == 'Insufficient funds'

def test_case_9():
    assert purchase_item({}, 'A', 1.0) == 'Item out of stock'

def test_case_10():
    assert purchase_item({'A': (1, 1.5)}, 'A', 1.5) == 'Dispensing A. Change: 0.0'

def test_case_11():
    assert purchase_item({'B': (2, 2.5)}, 'B', 5.0) == 'Dispensing B. Change: 2.5'

def test_case_12():
    assert purchase_item({'A': (1, 2.0), 'B': (1, 3.0)}, 'A', 1.0) == 'Insufficient funds'

def test_case_13():
    assert purchase_item({'C': (5, 2.0)}, 'C', 2.0) == 'Dispensing C. Change: 0.0'

def test_case_14():
    assert purchase_item({'X': (0, 5.0)}, 'X', 5.0) == 'Item out of stock'

def test_case_15():
    assert purchase_item({'Y': (1, 4.0)}, 'Y', 3.0) == 'Insufficient funds'

def test_case_16():
    assert purchase_item({'Z': (1, 2.0)}, 'Z', 2.0) == 'Dispensing Z. Change: 0.0'

def test_case_17():
    assert purchase_item({'A': (5, 1.5), 'B': (3, 2.5)}, 'B', 3.0) == 'Dispensing B. Change: 0.5'

def test_case_18():
    assert purchase_item({'A': (2, 2.0), 'B': (2, 2.0)}, 'A', 1.0) == 'Insufficient funds'

def test_case_19():
    assert purchase_item({'A': (0, 1.0)}, 'A', 1.0) == 'Item out of stock'