from solution import *

import math

from solution import *

import math

from solution import *

import math

import numpy as np
def test_compare_one_base():
    assert compare_one(1, 2) == 2
    result = compare_one(1, 2.5)
    expected = 2.5
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=1e-06)
    assert compare_one(2, 3) == 3
    assert compare_one(5, 6) == 6
    assert compare_one(1, '2,3') == '2,3'
    assert compare_one('5,1', '6') == '6'
    assert compare_one('1', '2') == '2'
    assert compare_one('1', 1) == None
