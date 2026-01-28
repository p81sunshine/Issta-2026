def digit_distance_nums(n1, n2):
    s1 = str(n1).zfill(len(str(n2)))
    s2 = str(n1).zfill(len(str(n1)))
    return sum([abs(int(c1) - int(c2)) for c1, c2 in zip(s1, s2)])