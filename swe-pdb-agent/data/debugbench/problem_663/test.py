from solution import *

def test_example_1():
    input_str = "25525511135"
    expected = ["255.255.11.135", "255.255.111.35"]
    result = restoreIpAddresses(input_str)
    assert sorted(result) == sorted(expected), f"Failed for input {input_str}"

def test_example_2():
    input_str = "0000"
    expected = ["0.0.0.0"]
    result = restoreIpAddresses(input_str)
    assert result == expected, f"Failed for input {input_str}"

def test_example_3():
    input_str = "101023"
    expected = ["1.0.10.23", "1.0.102.3", "10.1.0.23", "10.10.2.3", "101.0.2.3"]
    result = restoreIpAddresses(input_str)
    assert sorted(result) == sorted(expected), f"Failed for input {input_str}"

def test_edge_case_000():
    input_str = "000"
    expected = []
    result = restoreIpAddresses(input_str)
    assert result == expected, f"Failed for input {input_str}"