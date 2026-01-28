from solution import *

def test_example_1():
    assert capitalize_title("capiTalIze tHe titLe") == "Capitalize The Title", "Should capitalize first letter of words with length >=3"

def test_example_2():
    assert capitalize_title("First leTTeR of EACH Word") == "First Letter of Each Word", "Should handle mixed case and preserve 'of' as lowercase"

def test_example_3():
    assert capitalize_title("i lOve leetcode") == "i Love Leetcode", "Should lowercase single-character word and capitalize longer words"

def test_short_and_long_words():
    assert capitalize_title("a bc def") == "a bc Def", "Should handle words with exactly 3 characters and preserve short words"