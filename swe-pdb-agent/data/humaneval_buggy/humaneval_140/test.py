from solution import *

import math

from solution import *

import math

from solution import *

import math

import numpy as np
def test_fix_spaces_base():
    assert fix_spaces('Example') == 'Example'
    assert fix_spaces('Mudasir Hanif ') == 'Mudasir_Hanif_'
    assert fix_spaces('Yellow Yellow  Dirty  Fellow') == 'Yellow_Yellow__Dirty__Fellow'
    assert fix_spaces('Exa   mple') == 'Exa-mple'
    assert fix_spaces('   Exa 1 2 2 mple') == '-Exa_1_2_2_mple'
