from solution import *
import math

def test_all():
    n = 15
    pollardsRho = PollardsRhoFactorization(n)
    factor = pollardsRho.pollards_rho_factorization()
    assert factor not in [1, n]
    assert n % factor == 0
    assert factor is not None

    n = 13 * 17
    pollardsRho = PollardsRhoFactorization(n)
    factor = pollardsRho.pollards_rho_factorization()
    assert factor not in [1, n]
    assert n % factor == 0
    assert factor is not None

    n = 7919
    pollardsRho = PollardsRhoFactorization(n)
    factor = pollardsRho.pollards_rho_factorization()
    assert factor is None

    n = 100
    pollardsRho = PollardsRhoFactorization(n)
    factor = pollardsRho.pollards_rho_factorization()
    assert factor == 4

    n = 1
    pollardsRho = PollardsRhoFactorization(n)
    factor = pollardsRho.pollards_rho_factorization()
    assert factor is None

    n = 29 * 31
    pollardsRho = PollardsRhoFactorization(n)
    factor = pollardsRho.pollards_rho_factorization()
    assert factor in [29, 31]
    assert n % factor == 0
    assert factor is not None