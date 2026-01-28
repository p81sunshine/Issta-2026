from solution import *

def test_example_1():
    assert get_length_of_optimal_compression("aaabcccd", 2) == 4

def test_example_2():
    assert get_length_of_optimal_compression("aabbaa", 2) == 2

def test_example_3():
    assert get_length_of_optimal_compression("aaaaaaaaaaa", 0) == 3

def test_delete_all():
    assert get_length_of_optimal_compression("a", 1) == 0

def test_no_deletions_unique():
    assert get_length_of_optimal_compression("abcd", 0) == 4