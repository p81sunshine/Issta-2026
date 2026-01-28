from solution import *
import math

def test_all():
    assert double_consonant('th') == False
    assert double_consonant('ch') == False
    assert double_consonant('ll') == False
    assert double_consonant('gh') == True
    assert double_consonant('lt') == True
    assert double_consonant('ta') == False
    assert double_consonant('ab') == False
    assert double_consonant('xo') == True
    assert double_consonant('ae') == False
    assert double_consonant('cg') == True