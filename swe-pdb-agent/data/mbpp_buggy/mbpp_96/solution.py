def divisor(n):
  return sum(1 for i in range(1, n) if n % i == 0)

from solution import *
import math
import numpy as np
def test_divisor_base():
    assert divisor(15) == 4
    assert divisor(12) == 6
    assert divisor(9) == 3