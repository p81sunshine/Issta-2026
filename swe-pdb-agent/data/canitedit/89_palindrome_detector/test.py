from solution import *
import math

def test_all():
    assert isPalindrome("dad") == True
    assert isPalindrome("madamimadam") == True
    assert isPalindrome("a") == True
    assert isPalindrome("KaYaK") == True
    assert isPalindrome("CIVIC") == True
    
    assert isPalindrome("computer") == False
    assert isPalindrome("ab") == False