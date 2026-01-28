def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == "aaaaaaa"
    """


    mx_ch_cnt, ans = 0, None
    for word in words:
        ch_cnt = len(set(word)) 
        if ch_cnt >= mx_ch_cnt and (word < ans or ans is None):
            mx_ch_cnt, ans = ch_cnt, word
    return ans