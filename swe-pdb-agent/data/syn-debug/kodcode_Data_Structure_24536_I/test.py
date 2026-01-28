from solution import *

import math

from solution import *

import math

from solution import *

import math

from solution import RBTree

def test_range_query():
    rb = RBTree()
    children = [11, 2, 14, 1, 7, 15, 5, 8, 4]
    for child in children:
        rb.insert(child)

    assert sorted(rb.range_query(5, 14)) == sorted([5, 7, 8, 11, 14])
    assert sorted(rb.range_query(1, 8)) == sorted([1, 2, 4, 5, 7, 8])
    assert sorted(rb.range_query(10, 14)) == sorted([11, 14])
    assert sorted(rb.range_query(0, 3)) == sorted([1, 2])
    assert rb.range_query(16, 20) == []
    assert rb.range_query(0, 0) == []

def test_range_query_single_element():
    rb = RBTree()
    rb.insert(10)

    assert rb.range_query(10, 10) == [10]
    assert rb.range_query(5, 15) == [10]
    assert rb.range_query(10, 20) == [10]
    assert rb.range_query(0, 5) == []

def test_range_query_empty_tree():
    rb = RBTree()

    assert rb.range_query(5, 10) == []
    assert rb.range_query(0, 0) == []
    assert rb.range_query(-10, 10) == []