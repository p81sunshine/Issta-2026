def is_samepatterns(colors, patterns):
    if len(colors) != len(set(patterns)):
        return False
    pattern_color_dict = {pattern: set() for pattern in patterns}
    for color, pattern in zip(colors, patterns):
        pattern_color_dict[pattern].add(color)
    return all(len(pattern_color_dict[pattern]) == 1 for pattern in pattern_color_dict)