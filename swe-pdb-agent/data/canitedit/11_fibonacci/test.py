from solution import *
import math

def test_all():
    f = Fib()
    iterator = iter(f)

    assert next(iterator) == 1
    assert next(iterator) == 2
    assert next(iterator) == 3
    assert next(iterator) == 5

    iterator = iter(f)
    assert next(iterator) == 1
    assert next(iterator) == 2
    assert next(iterator) == 3
    assert next(iterator) == 5

    next_3 = list(iterator.next_n_fibs(3))
    assert next_3[0] == 8
    assert next_3[1] == 13
    assert next_3[2] == 21

    assert next(iterator) == 8