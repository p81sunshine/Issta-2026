from solution import *

def test_example_1():
    nums = [4,5,2,1]
    queries = [3,10,21]
    expected = [2,3,4]
    assert answerQueries(nums, queries) == expected, "Example 1 failed"

def test_example_2():
    nums = [2,3,4,5]
    queries = [1]
    expected = [0]
    assert answerQueries(nums, queries) == expected, "Example 2 failed"

def test_case_3():
    nums = [1,2,3]
    queries = [6]
    expected = [3]
    assert answerQueries(nums, queries) == expected, "Test case 3 failed"

def test_case_4():
    nums = [1,2]
    queries = [3]
    expected = [2]
    assert answerQueries(nums, queries) == expected, "Test case 4 failed"