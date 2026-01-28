import re
def occurance_substring(text, pattern):
    for match in re.finditer(pattern, text):
        s = match.start()
        e = match.end()
        if s == 0:
            e += 1
        return (text[s:e], s, e)
    return None