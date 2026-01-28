from solution import *
import math

def test_all():
    m = Matrix([[0, 1]])
    m.transpose()
    assert m.content == [[0], [1]]

    m = Matrix([[0, 1], [0, 1]])
    m.transpose()
    assert m.content == [[0, 0], [1, 1]]

    m = Matrix([[0, 2], [0, 1]])
    m.transpose()
    assert m.content == [[0, 0], [2, 1]]

    try:
        Matrix([[1], [2, 2]])
    except ValueError:
        assert True
    else:
        assert False

    try:
        Matrix([[1, 2, 3], [2, 2, 3]]).determinant()
    except AssertionError:
        assert True
    else:
        assert False

    try:
        Matrix([[1]]).determinant()
    except NotImplementedError:
        assert True
    else:
        assert False

    try:
        Matrix([[1], [2]]).determinant()
    except AssertionError:
        assert True
    else:
        assert False

    m = Matrix([[0, 2], [0, 1]])
    assert m.determinant() == 0

    m = Matrix([[2, 2], [0, 1]])
    assert m.determinant() == 2

    m = Matrix([[2, -1], [3, 1]])
    assert m.determinant() == 5

    m = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    assert m.determinant() == 0
    m = Matrix([[1, 2, 3], [4, -5, 6], [7, -8, 9]])
    assert m.determinant() == 24
    m = Matrix([[5, 5, 5], [4, 5, 6], [7, 8, 9]])
    assert m.determinant() == 0
    m = Matrix([[1, 9, 3], [4, -5, 9], [7, -8, 9]])
    assert m.determinant() == 279