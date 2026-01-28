from solution import *
import math

def test_all():
    m = MyVector(0, 0, 0)
    one = MyVector(1, 1, 1)
    v2 = MyVector(1, 1)
    v3 = MyVector(1, 0)
    v4 = MyVector(0, 1)
    v5 = MyVector(-1, 0)
    try:
        v2.cosine_similarity(m)
        assert False
    except:
        assert True

    try:
        v2.cosine_similarity(one)
        assert False
    except:
        assert True
        

    assert m.manhattan_distance(one) == 3
    assert abs(v3.cosine_similarity(v4)) < 0.01
    assert v3.cosine_similarity(v5) == -1