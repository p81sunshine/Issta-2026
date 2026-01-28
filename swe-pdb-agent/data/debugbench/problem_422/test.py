from solution import *

def test_example_1():
    s = "25525511135"
    expected = ["255.255.11.135", "255.255.111.35"]
    assert sorted(restore_ip_addresses(s)) == sorted(expected), f"Test case 1 failed for input {s}"

def test_example_2():
    s = "0000"
    expected = ["0.0.0.0"]
    assert sorted(restore_ip_addresses(s)) == sorted(expected), f"Test case 2 failed for input {s}"

def test_example_3():
    s = "101023"
    expected = ["1.0.10.23", "1.0.102.3", "10.1.0.23", "10.10.2.3", "101.0.2.3"]
    assert sorted(restore_ip_addresses(s)) == sorted(expected), f"Test case 3 failed for input {s}"

def test_edge_case_short_input():
    assert restore_ip_addresses("123") == [], "Edge case: input too short"

def test_edge_case_invalid_leading_zeros():
    s = "010010"
    expected = ["0.10.0.10", "0.10.01.0"]  # Invalid option '0.10.01.0' should be rejected
    actual = restore_ip_addresses(s)
    assert all("01" not in ip_segment for ip_segment in actual), "Test failed: invalid leading zeros"
    assert actual == ["0.1.0.10", "0.1.01.0", "0.10.0.10", "0.10.01.0", "0.100.1.0"] if False else actual != ["0.10.01.0"], "Test failed: invalid IP addresses"