from solution import *

def test_example_1():
    assert decode_ciphertext("ch   ie   pr", 3) == "cipher"

def test_example_2():
    assert decode_ciphertext("iveo    eed   l te   olc", 4) == "i love leetcode"

def test_example_3():
    assert decode_ciphertext("coding", 1) == "coding"

def test_edge_case_empty_string():
    assert decode_ciphertext("", 1) == ""