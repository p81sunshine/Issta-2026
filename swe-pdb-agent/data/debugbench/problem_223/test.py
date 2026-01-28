from solution import *

def test_example_1():
    assert minimum_partition("165462", 60) == 4, "Example 1 failed"

def test_example_2():
    assert minimum_partition("238182", 5) == -1, "Example 2 failed"

def test_split_case():
    assert minimum_partition("51", 5) == 2, "Split into two test failed"

def test_another_bug_case():
    assert minimum_partition("1234", 12) == 3, "Buggy case 1234 failed"

def test_single_digit():
    assert minimum_partition("3", 5) == 1, "Single digit valid failed"
    assert minimum_partition("6", 5) == -1, "Single digit invalid failed"