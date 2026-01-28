from solution import *

import math

from solution import *

import math

from solution import *

import math

import numpy as np
def test_match_parens_base():
    assert match_parens(['()(', ')']) == 'Yes'
    assert match_parens([')', ')']) == 'No'
    assert match_parens(['(()(())', '())())']) == 'No'
    assert match_parens([')())', '(()()(']) == 'Yes'
    assert match_parens(['(())))', '(()())((']) == 'Yes'
    assert match_parens(['()', '())']) == 'No'
    assert match_parens(['(()(', '()))()']) == 'Yes'
    assert match_parens(['((((', '((())']) == 'No'
    assert match_parens([')(()', '(()(']) == 'No'
    assert match_parens([')(', ')(']) == 'No'
    assert match_parens(['(', ')']) == 'Yes'
    assert match_parens([')', '(']) == 'Yes'
