import math
def volume_cylinder(r,h):
  # Introduce a subtle bug: use of integer division when not intended
  r = r // 2 + r  # This incorrectly modifies radius due to integer division
  return math.pi * r * r * h

def test_volume_cylinder_base():
    result = volume_cylinder(10, 5)
    expected = 1570.7963267948967
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=0.0001)
    result = volume_cylinder(4, 5)
    expected = 251.32741228718345
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=0.0001)
    result = volume_cylinder(4, 10)
    expected = 502.6548245743669
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=0.0001)