from solution import *
import math

def test_all():
    assert is_prime(5)
    assert not is_prime(16)
    assert not is_prime(1)

    curve1 = EllipticCurve(4,4,5)
    assert curve1.is_on_curve(1,3)
    assert curve1.is_on_curve(0,2)
    assert not curve1.is_on_curve(2,2)
    assert curve1.point_addition((1,3),(1,3)) == (2,0)
    assert curve1.point_addition((1,3),(0,2)) == (0,3)
    assert curve1.point_addition((0,2),(0,-2)) == (None, None)
    assert curve1.point_addition((0,2),(None,None)) == (0,2)
    assert curve1.point_addition((None,None),(None,None)) == (None,None)
    assert curve1.point_addition((None,None),(1,3)) == (1,3)

    assert curve1.point_multiplication(3,(1,3)) == curve1.point_addition(curve1.point_addition((1,3),(1,3)),(1,3))

    curve2 = EllipticCurve(4,4,3)
    assert curve2.point_addition((0,1),(0,1)) == (1,0)
    assert curve2.point_addition((0,1),(1,0)) == (0,2)
    assert curve2.point_addition((0,2),(0,2)) == (1,0)

    assert curve2.point_multiplication(2, (0, 1)) == curve2.point_addition((0, 1), (0, 1))
    assert curve2.point_multiplication(2, (1, 0)) == curve2.point_addition((1, 0), (1, 0))
    assert curve2.point_multiplication(2, (None,None)) == (None, None)
    assert curve2.point_multiplication(0, (None,None)) == (None, None)
    assert curve2.point_multiplication(0, (0,1)) == (None, None)
    assert curve2.point_double((0,1)) == curve2.point_addition((0,1),(0,1))
    assert curve2.point_double((0,2)) == curve2.point_addition((0,2),(0,2))

    curve3 = EllipticCurve(-11,-17,307)
    assert curve3.is_on_curve(2,131)
    assert curve3.mod_inverse(3) == 205
    assert curve3.mod_inverse(45) == 116
    assert curve3.point_multiplication(4,(2,131)) == (81,246)

    points = [(2,131),(10,140),(6,146),(29,148),(16,126)]
    for point in points:
        for i in range(3,20):
            n = i
            rd = 1 + ((i + 5) % (n-1))
            d, Q = curve3.generate_keypair(point,n,rd)
            assert curve3.validate_keypair(d,Q,point,n)

    points = [(2,131),(10,140),(6,146),(29,148),(16,126)]
    for point in points:
        for i in range(3,20):
            assert curve3.point_multiplication(i,point) == curve3.windowed_point_multiplication(i,point)