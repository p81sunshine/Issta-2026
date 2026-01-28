from solution import *

import math

from solution import *

import math

from solution import *

import math

import numpy as np
def test_is_nested_base():
    assert is_nested('[[]]') == True
    assert is_nested('[]]]]]]][[[[[]') == False
    assert is_nested('[][]') == False
    assert is_nested('[]') == False
    assert is_nested('[[[[]]]]') == True
    assert is_nested('[]]]]]]]]]]') == False
    assert is_nested('[][][[]]') == True
    assert is_nested('[[]') == False
    assert is_nested('[]]') == False
    assert is_nested('[[]][[') == True
    assert is_nested('[[][]]') == True
    assert is_nested('') == False
    assert is_nested('[[[[[[[[') == False
    assert is_nested(']]]]]]]]') == False
