from solution import *

import math

from solution import *

import math

from solution import *

import math

import numpy as np
def test_cycpattern_check_base():
    assert cycpattern_check('xyzw', 'xyw') == False
    assert cycpattern_check('yello', 'ell') == True
    assert cycpattern_check('whattup', 'ptut') == False
    assert cycpattern_check('efef', 'fee') == True
    assert cycpattern_check('abab', 'aabb') == False
    assert cycpattern_check('winemtt', 'tinem') == True
