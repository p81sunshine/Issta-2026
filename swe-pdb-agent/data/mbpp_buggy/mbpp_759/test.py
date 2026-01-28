from solution import *

import math

from solution import *

import math

from solution import *

import math

import numpy as np
def test_is_decimal_base():
    assert is_decimal('123.11') == True
    assert is_decimal('e666.86') == False
    assert is_decimal('3.124587') == False
    assert is_decimal('1.11') == True
    assert is_decimal('1.1.11') == False
