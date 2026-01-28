from solution import *

import math

from solution import *

import math

from solution import *

import math

import numpy as np
def test_insert_element_base():
    assert insert_element(['Red', 'Green', 'Black'], 'c') == ['c', 'Red', 'c', 'Green', 'c', 'Black']
    assert insert_element(['python', 'java'], 'program') == ['program', 'python', 'program', 'java']
    assert insert_element(['happy', 'sad'], 'laugh') == ['laugh', 'happy', 'laugh', 'sad']
