from solution import *
import math

def test_all():
    assert sum_of_prime_products_in_range(10, 20) == 12900
    assert sum_of_prime_products_in_range(10, 100) == 156402490
    assert sum_of_prime_products_in_range(1, 3) == 0
    assert sum_of_prime_products_in_range(50, 10) == 0
    assert sum_of_prime_products_in_range(13, 13) == 0