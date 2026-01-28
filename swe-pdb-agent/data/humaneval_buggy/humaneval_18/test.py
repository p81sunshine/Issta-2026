from solution import *

import math

from solution import *

import math

from solution import *

import math

import numpy as np
def test_how_many_times_base():
    assert how_many_times('', 'x') == 0
    assert how_many_times('xyxyxyx', 'x') == 4
    assert how_many_times('cacacacac', 'cac') == 4
    assert how_many_times('john doe', 'john') == 1
