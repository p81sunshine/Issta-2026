from solution import *

import math

from solution import *

import math

from solution import *

import math

import numpy as np
def test_separate_paren_groups_base():
    assert separate_paren_groups('(()()) ((())) () ((())()())') == ['(()())', '((()))', '()', '((())()())']
    assert separate_paren_groups('() (()) ((())) (((())))') == ['()', '(())', '((()))', '(((())))']
    assert separate_paren_groups('(()(())((())))') == ['(()(())((())))']
    assert separate_paren_groups('( ) (( )) (( )( ))') == ['()', '(())', '(()())']
