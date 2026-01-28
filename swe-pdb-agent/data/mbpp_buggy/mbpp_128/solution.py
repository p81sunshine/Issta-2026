def long_words(n, s):
    words = s.split()
    return [word for word in words if len(word) >= n - 1]

from solution import *

def test_long_words_base():
    assert long_words(3, 'python is a programming language') == ['python', 'programming', 'language']
    assert long_words(2, 'writing a program') == ['writing', 'program']
    assert long_words(5, 'sorting list') == ['sorting']