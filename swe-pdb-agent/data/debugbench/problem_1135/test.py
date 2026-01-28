from solution import *

def test_example_1():
    assert sortString("aaaabbbbcccc") == "abccbaabccba", "Example 1 failed"

def test_example_2():
    assert sortString("rat") == "art", "Example 2 failed"

def test_letters_modification():
    assert sortString("aab") == "aba", "Letters modification case failed"

def test_aaabbb_case():
    assert sortString("aaabbb") == "abbaab", "aaabbb case failed"