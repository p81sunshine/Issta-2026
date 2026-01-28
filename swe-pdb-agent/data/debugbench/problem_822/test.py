from solution import *

def test_example_1():
    s = "25525511135"
    expected = ["255.255.11.135", "255.255.111.35"]
    assert restore_ip_addresses(s) == expected, f"Failed for input {s}"

def test_example_2():
    s = "0000"
    expected = ["0.0.0.0"]
    assert restore_ip_addresses(s) == expected, f"Failed for input {s}"

def test_example_3():
    s = "101023"
    expected = ["1.0.10.23", "1.0.102.3", "10.1.0.23", "10.10.2.3", "101.0.2.3"]
    assert restore_ip_addresses(s) == expected, f"Failed for input {s}"

def test_invalid_length():
    s = "123"
    expected = []
    assert restore_ip_addresses(s) == expected, f"Failed for input {s}"