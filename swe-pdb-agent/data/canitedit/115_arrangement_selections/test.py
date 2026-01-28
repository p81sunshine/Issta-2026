from solution import *
import math

def test_all():
    assert combination(6, 3) == 20
    assert combination(3, 2) == 3
    assert combination(1, 1) == 1
    
    assert permutation(7, 4) == 840
    assert permutation(12, 7) == 3991680
    
    assert combination_unlimited_rep(7, 5) == 330
    assert combination_unlimited_rep(5, 3) == 21
    assert combination_unlimited_rep(10, 3) == 66
    assert combination_unlimited_rep(4, 3) == 15
    assert combination_unlimited_rep(20, 5) == 10626
    assert combination_unlimited_rep(15, 5) == 3876
    
    assert arrangement_restricted_rep(6, [3, 2, 1]) == 60
    assert arrangement_restricted_rep(8, [6, 2]) == 28
    assert arrangement_restricted_rep(10, [4, 2, 2, 2]) == 18900
    
    assert arrangement_unlimited_rep(3, 2) == 9