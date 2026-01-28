from solution import *

import math

from solution import *

import math

from solution import *

import math

import numpy as np
def test_make_palindrome_base():
    assert make_palindrome('') == ''
    assert make_palindrome('x') == 'x'
    assert make_palindrome('xyz') == 'xyzyx'
    assert make_palindrome('xyx') == 'xyx'
    assert make_palindrome('jerry') == 'jerryrrej'
