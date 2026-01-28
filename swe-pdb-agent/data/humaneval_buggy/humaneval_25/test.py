from solution import *

import math

from solution import *

import math

from solution import *

import math

import numpy as np
def test_factorize_base():
    assert factorize(2) == [2]
    assert factorize(4) == [2, 2]
    assert factorize(8) == [2, 2, 2]
    assert factorize(57) == [3, 19]
    assert factorize(3249) == [3, 3, 19, 19]
    assert factorize(185193) == [3, 3, 3, 19, 19, 19]
    assert factorize(20577) == [3, 19, 19, 19]
    assert factorize(18) == [2, 3, 3]
