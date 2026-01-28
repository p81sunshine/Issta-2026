from solution import *

def test_example_1():
    assert isIsomorphic("egg", "add") is True, "Example 1 failed"

def test_example_2():
    assert isIsomorphic("foo", "bar") is False, "Example 2 failed"

def test_example_3():
    assert isIsomorphic("paper", "title") is True, "Example 3 failed"

def test_buggy_slice_case():
    # This case exposes the t[:len(s)-1] bug in the buggy implementation
    assert isIsomorphic("ab", "ca") is True, "Buggy slice case failed"

def test_buggy_zip_length():
    # Buggy code would miss the last character in t during zip
    assert isIsomorphic("abc", "def") is True, "Buggy zip length case failed"

def test_buggy_mapping_conflict():
    # Buggy code would incorrectly return True where correct code returns False
    assert isIsomorphic("abac", "ccba") is False, "Buggy mapping conflict case failed"