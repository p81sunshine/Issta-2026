from solution import *

def test_example_1():
    s = "25525511135"
    expected = ["255.255.11.135", "255.255.111.35"]
    assert restoreIpAddresses(s) == expected, "Test case 1 failed"

def test_example_2():
    s = "0000"
    expected = ["0.0.0.0"]
    assert restoreIpAddresses(s) == expected, "Test case 2 failed"

def test_example_3():
    s = "101023"
    expected = ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
    assert restoreIpAddresses(s) == expected, "Test case 3 failed"

def test_edge_case_short():
    s = "123"
    expected = []
    assert restoreIpAddresses(s) == expected, "Edge case (short string) failed"

def test_edge_case_long():
    s = "1234567890123"
    expected = []
    assert restoreIpAddresses(s) == expected, "Edge case (long string) failed"