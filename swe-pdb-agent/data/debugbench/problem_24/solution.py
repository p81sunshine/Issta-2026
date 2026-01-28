from typing import List

def first_palindrome(words: List[str]) -> str:
    for i in words:
        if i == i[::-1]:
            return i
    return ""