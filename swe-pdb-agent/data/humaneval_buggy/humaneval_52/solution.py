def below_threshold(l: list, t: int):
    """Return True if all numbers in the list l are below threshold t.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    """

    return all(x < t for x in l if x != t)

def test_below_threshold_base():
    assert below_threshold([1, 2, 4, 10], 100) == True
    assert below_threshold([1, 20, 4, 10], 5) == False
    assert below_threshold([1, 20, 4, 10], 21) == True
    assert below_threshold([1, 20, 4, 10], 22) == True
    assert below_threshold([1, 8, 4, 10], 11) == True
    assert below_threshold([1, 8, 4, 10], 10) == False