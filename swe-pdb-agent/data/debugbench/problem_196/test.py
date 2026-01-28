from solution import *

def test_example_1():
    paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
    banned = ["hit"]
    assert mostCommonWord(paragraph, banned) == "ball", "Example 1 should return 'ball'"

def test_example_2():
    paragraph = "a."
    banned = []
    assert mostCommonWord(paragraph, banned) == "a", "Example 2 should return 'a'"

def test_banned_word_exclusion():
    paragraph = "apple apple banana orange"
    banned = ["apple"]
    assert mostCommonWord(paragraph, banned) == "banana", "Should return 'banana' after excluding 'apple'"

def test_multiple_words_with_banned():
    paragraph = "hello world hello there world"
    banned = ["world"]
    assert mostCommonWord(paragraph, banned) == "hello", "Should return 'hello' as it's the most frequent non-banned word"