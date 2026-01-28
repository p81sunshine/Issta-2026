from solution import *

import math

from solution import *

import math

from solution import *

import math

import numpy as np
def test_remove_Occ_base():
    assert remove_Occ('hello', 'l') == 'heo'
    assert remove_Occ('abcda', 'a') == 'bcd'
    assert remove_Occ('PHP', 'P') == 'H'
