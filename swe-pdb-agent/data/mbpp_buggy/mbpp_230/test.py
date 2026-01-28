from solution import *

import math

from solution import *

import math

from solution import *

import math

import numpy as np
def test_replace_blank_base():
    assert replace_blank('hello people', '@') == 'hello@people'
    assert replace_blank('python program language', '$') == 'python$program$language'
    assert replace_blank('blank space', '-') == 'blank-space'
