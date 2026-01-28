from solution import *

import math

from solution import *

import math

from solution import *

import math

import numpy as np
def test_is_palindrome_base():
    assert is_palindrome('') == True
    assert is_palindrome('aba') == True
    assert is_palindrome('aaaaa') == True
    assert is_palindrome('zbcd') == False
    assert is_palindrome('xywyx') == True
    assert is_palindrome('xywyz') == False
    assert is_palindrome('xywzx') == False
