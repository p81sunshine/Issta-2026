from solution import *

def test_example_1():
    paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
    banned = ["hit"]
    assert most_common_word(paragraph, banned) == "ball", "Should return 'ball' as most common non-banned word"

def test_example_2():
    paragraph = "a."
    banned = []
    assert most_common_word(paragraph, banned) == "a", "Should return 'a' as the only word"

def test_edge_case_multiple_spaces():
    paragraph = "   a   a   a   "
    banned = []
    assert most_common_word(paragraph, banned) == "a", "Should handle multiple spaces between/around words"

def test_case_with_mixed_punctuation():
    paragraph = "Hello!!! This; is, a test. Hello?"
    banned = ["test"]
    assert most_common_word(paragraph, banned) == "hello", "Should process mixed punctuation correctly"

def test_case_tie_resolution():
    paragraph = "a a b b"
    banned = []
    assert most_common_word(paragraph, banned) in ["a", "b"], "Should return any word in case of frequency tie"