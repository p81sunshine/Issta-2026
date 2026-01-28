from solution import *

def test_example_1():
    assert restoreIpAddresses("25525511135") == ["255.255.11.135","255.255.111.35"], "Failed for input '25525511135'"

def test_example_2():
    assert restoreIpAddresses("0000") == ["0.0.0.0"], "Failed for input '0000'"

def test_example_3():
    assert restoreIpAddresses("101023") == ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"], "Failed for input '101023'"

def test_edge_case_1234():
    assert restoreIpAddresses("1234") == ["1.2.3.4"], "Failed for input '1234'"

def test_edge_case_12345():
    assert restoreIpAddresses("12345") == ["1.2.3.45", "1.2.34.5", "1.23.4.5", "12.3.4.5"], "Failed for input '12345'"