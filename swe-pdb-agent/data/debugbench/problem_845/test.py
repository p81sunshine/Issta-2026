from solution import *

def test_example_1():
    assert get_length_of_optimal_compression("aaabcccd", 2) == 4, "Example 1: Optimal after deleting 'b' and 'd'"

def test_example_2():
    assert get_length_of_optimal_compression("aabbaa", 2) == 2, "Example 2: Optimal after deleting both 'b's"

def test_example_3():
    assert get_length_of_optimal_compression("aaaaaaaaaaa", 0) == 3, "Example 3: Cannot delete, returns 'a11'"

def test_edge_case_delete_all():
    assert get_length_of_optimal_compression("a", 1) == 0, "Edge case: Delete the only character"

def test_edge_case_complex_deletion():
    assert get_length_of_optimal_compression("aaabbb", 3) == 2, "Complex deletion case: Delete 3 characters to minimize"