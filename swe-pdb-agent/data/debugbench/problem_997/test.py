from solution import *

def test_example_1():
    s = "**|**|***|"
    queries = [[2, 5], [5, 9]]
    expected = [2, 3]
    assert platesBetweenCandles(s, queries) == expected, "Example 1 failed"

def test_example_2():
    s = "***|**|*****|**||**|*"
    queries = [[1, 17], [4, 5], [14, 17], [5, 11], [15, 16]]
    expected = [9, 0, 0, 0, 0]
    assert platesBetweenCandles(s, queries) == expected, "Example 2 failed"

def test_all_candles():
    s = "||||"
    queries = [[0, 3]]
    expected = [0]
    assert platesBetweenCandles(s, queries) == expected, "All candles test failed"

def test_no_candles():
    s = "***"
    queries = [[0, 2]]
    expected = [0]
    assert platesBetweenCandles(s, queries) == expected, "No candles test failed"

def test_overlapping_candles():
    s = "|*|*|"
    queries = [[0, 4]]
    expected = [2]
    assert platesBetweenCandles(s, queries) == expected, "Overlapping candles test failed"