from solution import *

def test_example_1():
    s = "25525511135"
    expected = ["255.255.11.135", "255.255.111.35"]
    assert restoreIpAddresses(s) == expected, "Failed for example 1"

def test_example_2():
    s = "0000"
    expected = ["0.0.0.0"]
    assert restoreIpAddresses(s) == expected, "Failed for example 2"

def test_example_3():
    s = "101023"
    expected = ["1.0.10.23", "1.0.102.3", "10.1.0.23", "10.10.2.3", "101.0.2.3"]
    assert restoreIpAddresses(s) == expected, "Failed for example 3"

def test_edge_case_empty():
    s = ""
    expected = []
    assert restoreIpAddresses(s) == expected, "Failed for empty string"

def test_edge_case_min_length():
    s = "1234"
    expected = ["1.2.3.4"]
    assert restoreIpAddresses(s) == expected, "Failed for minimal valid input"