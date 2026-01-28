from solution import *

import math

from solution import *

import math

from solution import *

import math

import numpy as np
def test_find_literals_base():
    assert find_literals('The quick brown fox jumps over the lazy dog.', 'fox') == ('fox', 16, 19)
    assert find_literals('Its been a very crazy procedure right', 'crazy') == ('crazy', 16, 21)
    assert find_literals('Hardest choices required strongest will', 'will') == ('will', 35, 39)
