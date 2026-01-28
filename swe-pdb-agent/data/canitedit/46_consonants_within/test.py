from solution import *
import math

def test_all():
    assert consonant_within('quem dixere chaos: rudis indigestaque moles') == 4
    assert consonant_within('sic erat instabilis tellus innabilis unda') == 4
    assert consonant_within('in nova fert animus mutatas dicere formas') == 2