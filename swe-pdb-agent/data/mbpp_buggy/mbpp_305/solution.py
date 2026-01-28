import re
def start_withp(words):
    for w in words:
        m = re.match("(P\w+)\W(P\w+)", w.lower())
        if m:
            return tuple(x.capitalize() for x in m.groups())