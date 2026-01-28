from solution import *

import math

from solution import *

import math

from solution import *

import math

import numpy as np
def test_bf_base():
    assert bf('Jupiter', 'Neptune') == ('Saturn', 'Uranus')
    assert bf('Jupiter', 'Neptune') == ('Saturn', 'Uranus')
    assert bf('Earth', 'Mercury') == ('Venus',)
    assert bf('Earth', 'Mercury') == ('Venus',)
    assert bf('Mercury', 'Uranus') == ('Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn')
    assert bf('Mercury', 'Uranus') == ('Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn')
    assert bf('Neptune', 'Venus') == ('Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus')
    assert bf('Neptune', 'Venus') == ('Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus')
    assert bf('Earth', 'Earth') == ()
    assert bf('Mars', 'Earth') == ()
    assert bf('Jupiter', 'Makemake') == ()
