import pytest
from acecode_evol_24161_llama3_1_instruct_45_code import is_valid_credit_card

def test_case_0():
    assert is_valid_credit_card(1234567812345670) == True

def test_case_1():
    assert is_valid_credit_card(4012888888881881) == True

def test_case_2():
    assert is_valid_credit_card(4222222222222) == True

def test_case_3():
    assert is_valid_credit_card(5105105105105100) == True

def test_case_4():
    assert is_valid_credit_card(6011514433546201) == True

def test_case_5():
    assert is_valid_credit_card(378282246310005) == True

def test_case_6():
    assert is_valid_credit_card(371449635398431) == True

def test_case_7():
    assert is_valid_credit_card(30569309025904) == True

def test_case_8():
    assert is_valid_credit_card(5555555555554444) == True

def test_case_9():
    assert is_valid_credit_card(1234567812345678) == False

def test_case_10():
    assert is_valid_credit_card(4111111111111112) == False

def test_case_11():
    assert is_valid_credit_card(4222222222223) == False

def test_case_12():
    assert is_valid_credit_card(5105105105105101) == False

def test_case_13():
    assert is_valid_credit_card(6011514433546202) == False

def test_case_14():
    assert is_valid_credit_card(378282246310006) == False

def test_case_15():
    assert is_valid_credit_card(371449635398432) == False

def test_case_16():
    assert is_valid_credit_card(30569309025905) == False

def test_case_17():
    assert is_valid_credit_card(5555555555554445) == False

def test_case_18():
    assert is_valid_credit_card(9876543210123456) == False

def test_case_19():
    assert is_valid_credit_card(1234567890123456) == False