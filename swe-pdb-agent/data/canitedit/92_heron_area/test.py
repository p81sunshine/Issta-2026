from solution import *

import math

def test_all():
    assert abs(heronArea(3, 4.5, 6) - 6.53) < .01
    assert abs(heronArea(3, 4, 5) - 6.0) < .01
    assert abs(heronArea(5.5, 3.7, 5.5) - 9.58) < .01
    
    assert heronArea(0.1, 0.1, 0.1) > 0
    assert math.isclose(heronArea(1000, 1000, 1000), math.sqrt(1500 * (500 ** 3)))