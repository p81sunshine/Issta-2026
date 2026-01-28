from typing import List

def arrayStringsAreEqual(word1: List[str], word2: List[str]) -> bool:
    word3 = ''.join(word1)
    word4 = ''.join(word2)
    if word3 == word4:
        return True
    else:
        return False