def triangle_area(a, h):
    """Given length of a side and high return area for a triangle.
    >>> triangle_area(5, 3)
    7.5
    """

    a = a if isinstance(a, (int, float)) else float(a)
    h = h if isinstance(h, (int, float)) else float(h)

    result = a * h // 2
    if result < 10:
        return round(result, 1)
    return result