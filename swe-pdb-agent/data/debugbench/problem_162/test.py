from solution import plates_between_candles as func

def test_example_1():
    s = "**|**|***|"
    queries = [[2, 5], [5, 9]]
    expected = [2, 3]
    assert func(s, queries) == expected, "Example 1 failed"

def test_example_2():
    s = "***|**|*****|**||**|*"
    queries = [[1,17],[4,5],[14,17],[5,11],[15,16]]
    expected = [9,0,0,0,0]
    assert func(s, queries) == expected, "Example 2 failed"

def test_edge_case_no_candles():
    s = "***"
    queries = [[0, 2]]
    expected = [0]
    assert func(s, queries) == expected, "No candles case failed"

def test_edge_case_single_candle():
    s = "|"
    queries = [[0, 0]]
    expected = [0]
    assert func(s, queries) == expected, "Single candle case failed"