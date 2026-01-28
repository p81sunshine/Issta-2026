def catalan_number(num):
    if num <= 1:
        return 1
    res_num = 1
    for i in range(num):
        res_num += catalan_number(i) * catalan_number(num - i - 1)
    return res_num

# Test Cases (Partial...):
from solution import *

import math
import numpy as np
def test_catalan_number_base():
    assert catalan_number(10) == 16796
    assert catalan_number(9) == 4862
    assert catalan_number(7) == 429