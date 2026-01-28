from typing import List

def array_strings_are_equal(word1: List[str], word2: List[str]) -> bool:
    word3 = ''.join(word1)
    word4 = ''.join(word2)
    return word3 == word4