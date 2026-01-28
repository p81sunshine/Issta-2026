from solution import *

import math

from solution import *

import math

from solution import *

import math

import numpy as np
def test_remove_vowels_base():
    assert remove_vowels('') == ''
    assert remove_vowels('abcdef\nghijklm') == 'bcdf\nghjklm'
    assert remove_vowels('fedcba') == 'fdcb'
    assert remove_vowels('eeeee') == ''
    assert remove_vowels('acBAA') == 'cB'
    assert remove_vowels('EcBOO') == 'cB'
    assert remove_vowels('ybcd') == 'ybcd'
