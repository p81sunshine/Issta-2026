def reverse_vowels(str1):
    is_vowel = lambda x: x in 'aeiouAEIOU'
    pos = [i for i, c in enumerate(str1) if is_vowel(c)]
    return ''.join(c if not is_vowel(c) else str1[pos.pop(0)] for c in str1)