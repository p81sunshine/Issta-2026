from solution import *
import math

def test_all():
    origin = Point(0, 0, None)
    one_one = Point(1, 1, Label("one"))
    two_two = Point(2, 2, Label("two"))
    two_two_neg = Point(-2, -2, Label("one"))
    three_three = Point(3, 3, Label("two"))
    three_three_2 = Point(3, 3, Label("two"))

    assert origin == origin
    assert origin != "bla"
    assert Label("one") == Label("one")
    assert Label("one") != Label("two")
    assert Label("one") != "bla"

    try:
        origin.knn([one_one], -1)
        assert False
    except AssertionError:
        assert True

    try:
        origin.knn([], 1)
        assert False
    except AssertionError:
        assert True

    try:
        one_one.knn([two_two], 1)
        assert False
    except AssertionError:
        assert True

    try:
        origin.knn([two_two], 3)
        assert False
    except AssertionError:
        assert True

    assert (
        origin.knn([one_one, two_two, two_two_neg, three_three, three_three_2], 1).name
        == "one"
    )
    assert (
        origin.knn([one_one, two_two, two_two_neg, three_three, three_three_2], 3).name
        == "one"
    )
    assert (
        origin.knn([one_one, two_two, two_two_neg, three_three, three_three_2], 5).name
        == "two"
    )