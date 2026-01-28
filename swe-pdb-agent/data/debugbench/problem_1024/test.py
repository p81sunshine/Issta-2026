from solution import *

def test_example_1():
    assert get_length_of_optimal_compression("aaabcccd", 2) == 4, "Example 1 failed"

def test_example_2():
    assert get_length_of_optimal_compression("aabbaa", 2) == 2, "Example 2 failed"

def test_example_3():
    assert get_length_of_optimal_compression("aaaaaaaaaaa", 0) == 3, "Example 3 failed"

def test_edge_case_all_delete():
    assert get_length_of_optimal_compression("abc", 3) == 0, "Edge case (all deleted) failed"

def test_edge_case_no_deletion_single_char():
    assert get_length_of_optimal_compression("a", 0) == 1, "Edge case (single char, no deletion) failed"