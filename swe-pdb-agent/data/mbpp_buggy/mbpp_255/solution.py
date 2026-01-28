from itertools import combinations_with_replacement
def combinations_colors(l, n):
    result = combinations_with_replacement(l, n)
    return [tuple(sorted(x)) for x in result]