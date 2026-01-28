from solution import *
import math

def test_all():
    a = House((0, 0), 3, 2)
    b = House((1, 1), 4, 3)
    c = House((2, 2), 2, 1)
    d = House((3, 3), 3, 2)
    e = House((4, 4), 4, 3)
    f = House((5, 5), 2, 1)
    g = House((6, 6), 100, 100)  # huge mansion!

    house1 = House((10, 20), 3, 2)
    assert house1.location == (10, 20)
    assert house1.bedrooms == 3
    assert house1.bathrooms == 2

    house2 = House((13, 24), 4, 3)
    assert house1.distance_to(
        house2) == 5.0

    other_houses = [House((1, 2), 2, 1), House((3, 4), 3, 2), House(
        (5, 6), 4, 3), House((7, 8), 2, 2), House((9, 10), 1, 1)]
    expected_price = (10000 * ((2 * 2) + 1) + 10000 * ((3 * 2) + 2) + 10000 *
                      ((4 * 2) + 3) + 10000 * ((2 * 2) + 2) + 10000 * ((1 * 2) + 1)) / 5
    assert house1.estimate_price(
        other_houses) == expected_price

    assert a.estimate_price([b, c, d, e, f, g]) == 80000
    assert a.estimate_price([b, c, d, e, f]) == 80000
    assert a.estimate_price([b,  f, g, c, d, e,]) == 80000
    assert a.estimate_price([f, b, c, d, e]) == 80000
    assert b.estimate_price([f, g]) == 1525000

    assert a.estimate_location([b, c, d, e, f, g]) == (3.0, 3.0)
    assert a.estimate_location([b, c, d, e, f]) == (3.0, 3.0)
    assert b.estimate_location([f, g]) == (5.5, 5.5)

    expected_location = ((1 + 3 + 5 + 7 + 9) / 5, (2 + 4 + 6 + 8 + 10) / 5)
    assert house1.estimate_location(
        other_houses) == expected_location

    houses_5 = [House((10, 20), 3, 2), House((30, 40), 2, 1), House(
        (50, 60), 4, 3), House((70, 80), 1, 1), House((90, 100), 2, 2)]
    expected_location_5 = ((10 + 30 + 50 + 70 + 90) / 5,
                           (20 + 40 + 60 + 80 + 100) / 5)
    assert house1.estimate_location(
        houses_5) == expected_location_5

    houses_3 = [House((10, 20), 3, 2), House(
        (30, 40), 2, 1), House((50, 60), 4, 3)]
    expected_location_3 = ((10 + 30 + 50) / 3, (20 + 40 + 60) / 3)
    assert house1.estimate_location(
        houses_3) == expected_location_3

    houses_more = [House((10, 20), 2, 1), House((30, 40), 3, 2), House((50, 60), 4, 3), House((70, 80), 2, 2), House((90, 100), 1, 1),
                   House((110, 120), 3, 3), House((130, 140), 2, 3), House((150, 160), 4, 4)]
    assert house1.estimate_location(houses_more) == (50.0, 60.0)