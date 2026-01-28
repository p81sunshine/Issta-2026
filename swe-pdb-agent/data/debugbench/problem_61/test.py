from solution import *

def test_example_1():
    assert partitionLabels("ababcbacadefegdehijhklij") == [9,7,8], "Example 1 failed"

def test_example_2():
    assert partitionLabels("eccbbbbdec") == [10], "Example 2 failed"

def test_single_char():
    assert partitionLabels("a") == [1], "Single character test failed"

def test_overlapping_case():
    assert partitionLabels("aabb") == [2,2], "Overlapping case failed"

def test_empty_string():
    assert partitionLabels("") == [], "Empty string edge case failed"