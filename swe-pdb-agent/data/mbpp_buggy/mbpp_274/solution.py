import math

def even_binomial_Coeff_Sum(n):
    total = 0
    for k in range(0, n + 1, 2):
        total += math.comb(n - 1, k)
    return total

# Test case for internal use
def test_even_binomial_Coeff_Sum_base():
    assert even_binomial_Coeff_Sum(4) == 8
    assert even_binomial_Coeff_Sum(6) == 32
    assert even_binomial_Coeff_Sum(2) == 2