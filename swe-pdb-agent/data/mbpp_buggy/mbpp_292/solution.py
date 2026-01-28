def find(n,m):
    return (n - 1) // m + 1 if n % m else n // m

    # Test Cases (Partial...):
from solution import *

import math
import numpy as np
def test_find_base():
    assert find(10, 3) == 3
    assert find(4, 2) == 2
    assert find(20, 5) == 4