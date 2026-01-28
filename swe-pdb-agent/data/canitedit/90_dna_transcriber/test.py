from solution import *
import math

def test_all():
    assert transcribe("TACTAGA") == "AUGAUCU"
    assert transcribe("C") == "G"
    assert transcribe("GCTAT") == "CGAUA"
    assert transcribe("") == ""