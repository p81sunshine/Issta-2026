from solution import *

def test_example_1():
    assert restore_ip_addresses("25525511135") == ["255.255.11.135", "255.255.111.35"], "Failed for '25525511135'"

def test_example_2():
    assert restore_ip_addresses("0000") == ["0.0.0.0"], "Failed for '0000'"

def test_example_3():
    expected = ["1.0.10.23", "1.0.102.3", "10.1.0.23", "10.10.2.3", "101.0.2.3"]
    assert restore_ip_addresses("101023") == expected, "Failed for '101023'"

def test_edge_case_invalid_length():
    assert restore_ip_addresses("123") == [], "Should return empty for length < 4"
    assert restore_ip_addresses("1234567890") == [], "Should return empty for length > 12"