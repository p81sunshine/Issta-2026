from solution import *
import math

def test_all():
    assert containsSpecialChar('1243i4u@') == True
    assert containsSpecialChar('pqighp') == False
    assert containsSpecialChar('') == False
    assert containsSpecialChar('!@#$') == True

    assert isPasswordStrong('ThisPAsswordIsStrong!') == True
    assert isPasswordStrong('password') == False
    assert isPasswordStrong('$%^&\"') == False
    assert isPasswordStrong('hello') == False
    assert isPasswordStrong('') == False
    assert isPasswordStrong('1234567890') == False
    assert isPasswordStrong('1234567890!@#$%^&*()') == True
    assert isPasswordStrong('blarg#lzxcvbnm') == True