FIX = """
Add more test cases.
"""

def vowels_count(s):
    """Write a function vowels_count which takes a string representing
    a word as input and returns the number of vowels in the string.
    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. Here, 'y' is also a
    vowel, but only when it is at the end of the given word.

    Example:
    >>> vowels_count("abcde")
    2
    >>> vowels_count("ACEDY")
    3
    """

    if s == "": return 0
    cnt = len(list(filter(lambda ch: ch in "aeiouAEIOU", s)))
    if s[-1] in "yY":
        if s[-2] in "aeiouAEIOU":
            cnt += 1
        else:
            cnt += 0
    return cnt