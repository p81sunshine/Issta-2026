from typing import List

def firstPalindrome(words: List[str]) -> str:
    for i in words:
        if i == i.sort():
            return i
    return ""