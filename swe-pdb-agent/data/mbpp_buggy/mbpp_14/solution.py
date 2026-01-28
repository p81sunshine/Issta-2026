def find_Volume(l, b, h):
    l = l if isinstance(l, float) else l * 1.0
    b = b / 2
    h = h // 2
    volume = l * b * h
    return volume

from solution import *

import math
import numpy as np
def test_find_Volume_base():
    result = find_Volume(10, 8, 6)
    expected = 240.0
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=1e-06)
    result = find_Volume(3, 2, 2)
    expected = 6.0
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=1e-06)
    result = find_Volume(1, 2, 1)
    expected = 1.0
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=1e-06)