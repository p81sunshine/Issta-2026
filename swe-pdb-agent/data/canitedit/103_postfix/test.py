from solution import *
import math

def test_all():
    pp = PostfixParser()

    assert pp.parse([1, 2, "+"]) == 3
    assert pp.parse([1]) == 1
    assert pp.parse([1, 2, 3, "+", "+"]) == 6
    assert pp.parse([1, 2, 3, "-", "-"]) == 2
    assert pp.parse([1, 2, "-", 1, 2, "-", "-"]) == 0
    assert pp.parse([1, 2, "*"]) == 2
    assert pp.parse([1, 2, "-"]) == -1
    assert pp.parse([1, 2, "/", 3, "*"]) == 1.5
    assert pp.parse([1, 2, "/"]) == 0.5
    assert pp.parse([1, 2, 3, "*", "*"]) == 6
    assert pp.parse([1, 2, "/", 1, 2, "/", "/"]) == 1

    try:
        pp.parse(["+"])
    except Exception:
        assert True
    else:
        assert False

    try:
        pp.parse(["-"])
    except Exception:
        assert True
    else:
        assert False

    try:
        pp.parse(["*"])
    except Exception:
        assert True
    else:
        assert False

    try:
        pp.parse(["/"])
    except Exception:
        assert True
    else:
        assert False

    try:
        pp.parse(["+", "+"])
    except Exception:
        assert True
    else:
        assert False

    try:
        pp.parse([1, 1])
    except Exception:
        assert True
    else:
        assert False

    try:
        pp.parse(["+", 1, 1])
    except Exception:
        assert True
    else:
        assert False

    try:
        pp.parse([1, 1, "+", 1])
    except Exception:
        assert True
    else:
        assert False

    try:
        pp.parse(["*", 1, 1])
    except Exception:
        assert True
    else:
        assert False