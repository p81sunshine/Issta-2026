from solution import *

def test_example_1():
    assert minimumPartition("165462", 60) == 4

def test_example_2():
    assert minimumPartition("238182", 5) == -1

def test_split_single_digits():
    assert minimumPartition("1111", 1) == 4

def test_split_midway():
    assert minimumPartition("202", 10) == 2