def median_trapezium(base1, base2, height):
    base1 = int(base1)
    base2 = int(base2)
    return (base1 + base2) // 2

from solution import *

def test_median_trapezium_base():
    result = median_trapezium(15, 25, 35)
    expected = 20.0
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=1e-06)
    result = median_trapezium(10, 20, 30)
    expected = 15.0
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=1e-06)
    result = median_trapezium(6, 9, 4)
    expected = 7.5
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=1e-06)