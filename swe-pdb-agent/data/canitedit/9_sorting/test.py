from solution import *
import math

def test_all():
    s = Sorter()
    empty = []
    ones = [1, 1]
    one_three_two = [1, 3, 2]
    sorted = [1, 2, 3]

    s.sort(empty)
    s.sort(ones)
    s.sort(one_three_two)
    s.sort(sorted)

    assert len(empty) == 0
    assert len(ones) == 2
    assert len(one_three_two) == 3
    assert len(sorted) == 3

    assert ones[0] == 1
    assert ones[1] == 1

    assert one_three_two[0] == 1
    assert one_three_two[1] == 2
    assert one_three_two[2] == 3

    assert sorted[0] == 1
    assert sorted[1] == 2
    assert sorted[2] == 3