from solution import *

def test_example_1():
    assert get_length_of_optimal_compression("aaabcccd", 2) == 4, "Failed on example 1: optimal deletion should yield length 4"

def test_example_2():
    assert get_length_of_optimal_compression("aabbaa", 2) == 2, "Failed on example 2: optimal deletion should yield length 2"

def test_example_3():
    assert get_length_of_optimal_compression("aaaaaaaaaaa", 0) == 3, "Failed on example 3: no deletions allowed should yield length 3"

def test_delete_all():
    assert get_length_of_optimal_compression("abc", 3) == 0, "Failed on delete-all case: should return 0 when all characters are deleted"

def test_all_unique():
    assert get_length_of_optimal_compression("abcd", 0) == 4, "Failed on all-unique case: no deletions should return original length"

def test_optimal_deletion_for_compression():
    assert get_length_of_optimal_compression("aaabbb", 3) == 2, "Failed on custom case: optimal deletion should compress to length 2"