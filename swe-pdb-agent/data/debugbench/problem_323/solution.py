from typing import List

def array_strings_are_equal(word1: List[str], word2: List[str]) -> bool:
    word3 = concat(word1)
    word4 = concat(word2)
    if word3 == word4:
        return True
    else:
        return False