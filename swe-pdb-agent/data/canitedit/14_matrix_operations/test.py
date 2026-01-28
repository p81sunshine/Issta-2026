from solution import *
import math

def test_all():
    m1 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    m2 = [
        [9, 9, 9],
        [8, 8, 8],
        [0, 1, -2]
    ]

    m3 = [
        [-1, 5, 0],
        [2, -8, 7],
        [4, 3, -2],
        [0, 6, 1]
    ]

    mat1 = Matrix(m1)
    mat2 = Matrix(m2)
    mat3 = Matrix(m3)

    try:
        mat1.add(mat3)
        assert False
    except ValueError:
        pass

    try:
        mat2.add(mat3)
        assert False
    except ValueError:
        pass

    try:
        mat3.subtract(mat1)
        assert False
    except ValueError:
        pass

    try:
        mat2.subtract(mat3)
        assert False
    except ValueError:
        pass

    assert mat1.add(mat2).matrix == [[10, 11, 12],
                                     [12, 13, 14],
                                     [7, 9, 7]]

    assert mat2.subtract(mat1).matrix == [[8, 7, 6],
                                          [4, 3, 2],
                                          [-7, -7, -11]]

    assert mat1.subtract(mat2).matrix == [[-8, -7, -6],
                                          [-4, -3, -2],
                                          [7, 7, 11]]

    # check if same_size exists. acceptable if either is a class method or a function
    assert hasattr(Matrix, 'same_size') or callable(
        same_size), "You have not defined a function or method called same_size"

    # try out transpose
    assert mat1.transpose().matrix == [[1, 4, 7],
                                       [2, 5, 8],
                                       [3, 6, 9]]