from solution import *
import math

def test_all():
    assert max_sublstay_sum([-2, -3, 4, -1, -2, 1, 5, -3]) == (7, 2, 6)
    assert max_sublstay_sum([-2, -3, -4, -1, -2, -1, -5, -3]) == (-1, 3, 3)
    assert max_sublstay_sum([1, 2, 3, 4, 5]) == (15, 0, 4)
    assert max_sublstay_sum([4]) == (4, 0, 0)
    assert max_sublstay_sum([1, -2, 3, 10, -4, 7, 2, -5]) == (18, 2, 6)