from solution import *

import math

from solution import *

import math

from solution import *

import math

import numpy as np
def test_differ_At_One_Bit_Pos_base():
    assert differ_At_One_Bit_Pos(13, 9) == True
    assert differ_At_One_Bit_Pos(15, 8) == False
    assert differ_At_One_Bit_Pos(2, 4) == False
    assert differ_At_One_Bit_Pos(2, 3) == True
    assert differ_At_One_Bit_Pos(5, 1) == True
    assert differ_At_One_Bit_Pos(1, 5) == True
