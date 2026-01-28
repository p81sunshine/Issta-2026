from solution import *
import math

def test_all():
    e = Empty()
    c1 = Cons(1, e)
    c2 = Cons(2, c1)
    duplicates = Cons(1, Cons(2, Cons(1, e)))
    assert e == e.remove(1)
    assert e == e.sort()
    assert e.insert(1).first == 1
    assert e.insert(1).rest == e

    assert c1.first == 1
    assert c1.rest == e
    assert c2.first == 2
    assert c2.rest.first == 1

    assert c1.sort().first == 1
    assert c1.sort().rest == e

    assert c2.sort().first == 1
    assert c2.sort().rest.first == 2
    assert c2.sort().rest.rest == e

    assert c1.remove(1) == e
    assert c2.remove(2).first == 1

    assert duplicates.remove(1).first == 2
    assert duplicates.remove(1).rest.first == 1

    c5 = Cons(5, Cons(4, Cons(3, Cons(2, Cons(1, e)))))
    assert c5.sort().first == 1
    assert c5.remove(3).first == 5

    c6 = Cons(7, Cons(6, Cons(2, Cons(4, Cons(3, Cons(2, Cons(1, e)))))))
    c7 = c6.insert(8)
    assert c7.first == 7
    # last one is 8
    assert c7.rest.rest.rest.rest.rest.rest.rest.first == 8
    c8 = c7.insert(1)
    assert c8.first == 1