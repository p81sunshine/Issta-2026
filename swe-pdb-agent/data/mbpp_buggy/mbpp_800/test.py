from solution import *

import math

from solution import *

import math

from solution import *

import math

import numpy as np
def test_remove_all_spaces_base():
    assert remove_all_spaces('python  program') == 'pythonprogram'
    assert remove_all_spaces('python   programming    language') == 'pythonprogramminglanguage'
    assert remove_all_spaces('python                     program') == 'pythonprogram'
    assert remove_all_spaces('   python                     program') == 'pythonprogram'
