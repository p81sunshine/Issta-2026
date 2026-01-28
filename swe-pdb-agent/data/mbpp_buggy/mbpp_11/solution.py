def remove_Occ(s, ch):
    first_index = s.find(ch)
    last_index = s.rfind(ch)

    if first_index == -1:
        return s

    s = s[:first_index] + s[first_index+1:]
    s = s[:last_index] + s[last_index+1:]
    return s