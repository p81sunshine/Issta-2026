from solution import *
import math

def test_all():
    assert vowel_count('adspirate meis primaque ab origine mundi') == 15
    assert vowel_count('dsprt ms prmq b rgn mnd') == 0
    assert vowel_count('') == 0
    assert vowel_count('In nova fert animus mut@tas dicere 7formas;') == 14
    assert vowel_count('in nova fert animus mutatas dicere formas') == 15