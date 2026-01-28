def same_chars(s0: str, s1: str):
    """
    Check if two words have the same characters.
    >>> same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc')
    True
    >>> same_chars('abcd', 'dddddddabc')
    True
    >>> same_chars('dddddddabc', 'abcd')
    True
    >>> same_chars('eabcd', 'dddddddabc')
    False
    >>> same_chars('abcd', 'dddddddabce')
    False
    >>> same_chars('eabcdzzzz', 'dddzzzzzzzddddabc')
    False
    """

    s0 = s0[:8]
    s1 = s1[:8]

    from collections import Counter
    count0 = Counter(s0)
    count1 = Counter(s1)
    
    for char in count0:
        if count0[char] != count1.get(char, 0):
            return False
    return True