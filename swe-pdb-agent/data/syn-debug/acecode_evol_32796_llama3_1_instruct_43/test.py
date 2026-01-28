import pytest
from acecode_evol_32796_llama3_1_instruct_43_code import calculate_prime_factor_frequency

def test_case_0():
    assert calculate_prime_factor_frequency(1) == {}

def test_case_1():
    assert calculate_prime_factor_frequency(2) == {2: 1}

def test_case_2():
    assert calculate_prime_factor_frequency(3) == {3: 1}

def test_case_3():
    assert calculate_prime_factor_frequency(4) == {2: 2}

def test_case_4():
    assert calculate_prime_factor_frequency(5) == {5: 1}

def test_case_5():
    assert calculate_prime_factor_frequency(6) == {2: 1, 3: 1}

def test_case_6():
    assert calculate_prime_factor_frequency(8) == {2: 3}

def test_case_7():
    assert calculate_prime_factor_frequency(9) == {3: 2}

def test_case_8():
    assert calculate_prime_factor_frequency(10) == {2: 1, 5: 1}

def test_case_9():
    assert calculate_prime_factor_frequency(12) == {2: 2, 3: 1}

def test_case_10():
    assert calculate_prime_factor_frequency(15) == {3: 1, 5: 1}

def test_case_11():
    assert calculate_prime_factor_frequency(18) == {2: 1, 3: 2}

def test_case_12():
    assert calculate_prime_factor_frequency(20) == {2: 2, 5: 1}

def test_case_13():
    assert calculate_prime_factor_frequency(28) == {2: 2, 7: 1}

def test_case_14():
    assert calculate_prime_factor_frequency(30) == {2: 1, 3: 1, 5: 1}

def test_case_15():
    assert calculate_prime_factor_frequency(45) == {3: 2, 5: 1}

def test_case_16():
    assert calculate_prime_factor_frequency(60) == {2: 2, 3: 1, 5: 1}

def test_case_17():
    assert calculate_prime_factor_frequency(100) == {2: 2, 5: 2}

def test_case_18():
    assert calculate_prime_factor_frequency(315) == {3: 2, 5: 1, 7: 1}

def test_case_19():
    assert calculate_prime_factor_frequency(1000000000) == {2: 9, 5: 9}