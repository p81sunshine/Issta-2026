from solution import *

import math

from solution import *

import math

from solution import *

import math

import numpy as np
def test_do_algebra_base():
    assert do_algebra(['**', '*', '+'], [2, 3, 4, 5]) == 37
    assert do_algebra(['+', '*', '-'], [2, 3, 4, 5]) == 9
    assert do_algebra(['//', '*'], [7, 3, 4]) == 8
