from solution import *

def test_example_1():
    assert restoreIpAddresses("25525511135") == ["255.255.11.135", "255.255.111.35"], "Failed for example 1"

def test_example_2():
    assert restoreIpAddresses("0000") == ["0.0.0.0"], "Failed for example 2"

def test_example_3():
    expected = ["1.0.10.23", "1.0.102.3", "10.1.0.23", "10.10.2.3", "101.0.2.3"]
    assert restoreIpAddresses("101023") == expected, "Failed for example 3"

def test_short_valid():
    assert restoreIpAddresses("1234") == ["1.2.3.4"], "Failed for 4-digit input"

def test_short_invalid():
    assert restoreIpAddresses("123") == [], "Failed for 3-digit input"

def test_long_string():
    expected = ["1.2.3.45", "1.2.34.5", "1.23.4.5", "12.3.4.5"]
    assert restoreIpAddresses("12345") == expected, "Failed for input 12345"

def test_length_exceed():
    assert restoreIpAddresses("1234567890123") == [], "Failed for input longer than 12 characters"