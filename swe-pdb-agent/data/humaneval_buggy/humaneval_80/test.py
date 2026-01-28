from solution import *

import math

from solution import *

import math

from solution import *

import math

import numpy as np
def test_is_happy_base():
    assert is_happy('a') == False
    assert is_happy('aa') == False
    assert is_happy('abcd') == True
    assert is_happy('aabb') == False
    assert is_happy('adb') == True
    assert is_happy('xyy') == False
    assert is_happy('iopaxpoi') == True
    assert is_happy('iopaxioi') == False
