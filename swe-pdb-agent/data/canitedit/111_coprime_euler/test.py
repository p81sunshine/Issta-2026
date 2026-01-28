from solution import *
import math

def test_all():
    assert gcd(1,1) == 1
    assert gcd(1,2) == 1
    assert gcd(3,7) == 1
    assert gcd(4,2) == 2
    assert gcd(3123,312) == 3
    assert gcd(25,45) == 5
    assert gcd(987, 987) == 987

    for i in range(1,50):
        for j in range(1,50):
            assert gcd(i,j) == math.gcd(i,j)

    assert euler_totient(18) == 6
    assert euler_totient(5913) == 3888
    assert euler_totient(1) == 1

    assert check_coprime_euler(1,1) == False

    # recall: two numbers are coprime if and only if their gcd is 1
    for i in range(1,50):
        for j in range(2,50):
            assert (gcd(i,j) == 1) == check_coprime_euler(i,j)