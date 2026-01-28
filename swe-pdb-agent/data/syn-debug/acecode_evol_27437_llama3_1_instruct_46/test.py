import pytest
from acecode_evol_27437_llama3_1_instruct_46_code import is_prime, filter_primes

def test_case_0():
    assert filter_primes([2, 3, 4, 5, 6, 7, 8, 19.5, 'print(Hello world)', 11, 13, 14]) == [2, 3, 5, 7]

def test_case_1():
    assert filter_primes([-1, -2, -3, 'hello', 5, 7]) == []

def test_case_2():
    assert filter_primes([4, 6, 8, 9, 10, 11, 'error', 13]) == [11]

def test_case_3():
    assert filter_primes([2.5, 3.1, 4, 5, 6]) == [5]

def test_case_4():
    assert filter_primes([2, 3, 5, 7, 'stop', 11]) == [2, 3, 5, 7]

def test_case_5():
    assert filter_primes([1, 2, 3, 4, 5, 6, -7, 8, 9]) == [2, 3, 5]

def test_case_6():
    assert filter_primes([10, 12, 14, 15, 'oops', 17, 19]) == []

def test_case_7():
    assert filter_primes([]) == []

def test_case_8():
    assert filter_primes(['not a number', 3, 4, 5]) == []

def test_case_9():
    assert filter_primes([10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 'break']) == [11, 13, 17, 19]

def test_case_10():
    assert filter_primes([22, 23, 24, 25, 26, 27, 28, 'string', 29]) == [23]

def test_case_11():
    assert filter_primes([-10, -11, 'text', 3.5]) == []

def test_case_12():
    assert filter_primes([0, 1, 2, 3, 'error']) == [2, 3]

def test_case_13():
    assert filter_primes([1.1, 1.2, 1.3, 1.4, 'stop', 5]) == []

def test_case_14():
    assert filter_primes([3, 4, 5, 6, 7, -8, 'failure']) == [3, 5, 7]

def test_case_15():
    assert filter_primes(['begin', 4, 6, 8, 10]) == []

def test_case_16():
    assert filter_primes([11, 12, 13, 14, 15, 16, 'halt']) == [11, 13]

def test_case_17():
    assert filter_primes([4.5, 5.5, 6.5, 7.5, 'end']) == []

def test_case_18():
    assert filter_primes([2, 3, 'foo', 17, 19, 23]) == [2, 3]