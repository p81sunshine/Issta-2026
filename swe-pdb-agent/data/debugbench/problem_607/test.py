from solution import *

def test_example_1():
    s = "25525511135"
    expected = ["255.255.11.135", "255.255.111.35"]
    actual = restoreIpAddresses(s)
    assert actual == expected, f"Failed for input {s}"

def test_example_2():
    s = "0000"
    expected = ["0.0.0.0"]
    actual = restoreIpAddresses(s)
    assert actual == expected, f"Failed for input {s}"

def test_example_3():
    s = "101023"
    expected = ["1.0.10.23", "1.0.102.3", "10.1.0.23", "10.10.2.3", "101.0.2.3"]
    actual = restoreIpAddresses(s)
    assert actual == expected, f"Failed for input {s}"

def test_edge_case_short_string():
    s = "111"
    expected = []
    actual = restoreIpAddresses(s)
    assert actual == expected, f"Failed for short input {s}"

def test_edge_case_invalid_leading_zeros():
    s = "00000"
    expected = []
    actual = restoreIpAddresses(s)
    assert actual == expected, f"Failed for invalid leading zeros input {s}"