from solution import *

def test_example_1():
    assert restore_ip_addresses("25525511135") == ["255.255.11.135", "255.255.111.35"], "Example 1 failed"

def test_example_2():
    assert restore_ip_addresses("0000") == ["0.0.0.0"], "Example 2 failed"

def test_example_3():
    assert restore_ip_addresses("101023") == ["1.0.10.23", "1.0.102.3", "10.1.0.23", "10.10.2.3", "101.0.2.3"], "Example 3 failed"

def test_edge_case_invalid_length():
    assert restore_ip_addresses("123") == [], "Invalid length input should return empty list"

def test_edge_case_valid_short():
    assert restore_ip_addresses("1111") == ["1.1.1.1"], "Valid short input failed"