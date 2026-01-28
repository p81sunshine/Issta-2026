from solution import *
import pytest

def test_example_1(capsys):
    result = maxPerformance(6, [2,10,3,1,5,8], [5,4,3,9,7,2], 2)
    assert result == 60, "Example 1 failed"
    captured = capsys.readouterr()
    assert captured.out == "", "No output should be printed"

def test_example_2(capsys):
    result = maxPerformance(6, [2,10,3,1,5,8], [5,4,3,9,7,2], 3)
    assert result == 68, "Example 2 failed"
    captured = capsys.readouterr()
    assert captured.out == "", "No output should be printed"

def test_example_3(capsys):
    result = maxPerformance(6, [2,10,3,1,5,8], [5,4,3,9,7,2], 4)
    assert result == 72, "Example 3 failed"
    captured = capsys.readouterr()
    assert captured.out == "", "No output should be printed"

def test_edge_case_1(capsys):
    result = maxPerformance(1, [5], [3], 1)
    assert result == 15, "Edge case 1 failed"
    captured = capsys.readouterr()
    assert captured.out == "", "No output should be printed"