def are_almost_equal(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False
        if s1 == s2:
            return True
    diff = []
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            diff.append([s1[i], s2[i]])
    if len(diff) == 2 and diff[0] == diff[-1][::-1]:
        return True
    else:
        return False