from solution import *

import math

from solution import *

import math

from solution import *

import math

import numpy as np
def test_even_odd_palindrome_base():
    assert even_odd_palindrome(123) == (8, 13)
    assert even_odd_palindrome(12) == (4, 6)
    assert even_odd_palindrome(3) == (1, 2)
    assert even_odd_palindrome(63) == (6, 8)
    assert even_odd_palindrome(25) == (5, 6)
    assert even_odd_palindrome(19) == (4, 6)
    assert even_odd_palindrome(9) == (4, 5)
    assert even_odd_palindrome(1) == (0, 1)
