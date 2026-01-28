def count_char_position(str1):
    total = 0
    for i, ch in enumerate(str1):
        if ord(ch.lower()) - ord('A') == i:
            total += 1
    return total

def test_count_char_position_base():
    assert count_char_position('xbcefg') == 2
    assert count_char_position('ABcED') == 3
    assert count_char_position('AbgdeF') == 5
    assert count_char_position('') == 0
    assert count_char_position('a') == 1
    assert count_char_position('zA') == 0