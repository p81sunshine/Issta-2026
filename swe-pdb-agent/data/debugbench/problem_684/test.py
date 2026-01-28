from solution import *

def test_example_1():
    input_str = "25525511135"
    expected = ["255.255.11.135", "255.255.111.35"]
    assert sorted(restoreIpAddresses(input_str)) == sorted(expected)

def test_example_2():
    input_str = "0000"
    expected = ["0.0.0.0"]
    assert sorted(restoreIpAddresses(input_str)) == sorted(expected)

def test_example_3():
    input_str = "101023"
    expected = ["1.0.10.23", "1.0.102.3", "10.1.0.23", "10.10.2.3", "101.0.2.3"]
    assert sorted(restoreIpAddresses(input_str)) == sorted(expected)

def test_edge_case_short_string():
    input_str = "123"
    expected = []
    assert restoreIpAddresses(input_str) == expected

def test_edge_case_single_segment():
    input_str = "1111"
    expected = ["1.1.1.1"]
    assert sorted(restoreIpAddresses(input_str)) == sorted(expected)