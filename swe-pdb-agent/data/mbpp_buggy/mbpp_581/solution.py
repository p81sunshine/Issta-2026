def surface_Area(b, s):
    from math import sqrt
    slant = sqrt((b / 2) ** 2 + s ** 2)
    lateral_area = 2 * b * slant
    base_area = b ** 2
    return lateral_area + base_area