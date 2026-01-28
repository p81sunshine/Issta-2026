from solution import *

def test_example_1():
    assert get_length_of_optimal_compression("aaabcccd", 2) == 4

def test_example_2():
    assert get_length_of_optimal_compression("aabbaa", 2) == 2

def test_example_3():
    assert get_length_of_optimal_compression("aaaaaaaaaaa", 0) == 3

def test_all_deletions():
    assert get_length_of_optimal_compression("abc", 3) == 0

def test_single_character_no_deletion():
    assert get_length_of_optimal_compression("a", 0) == 1

def test_two_characters_with_deletion():
    assert get_length_of_optimal_compression("ab", 1) == 1