from solution import *
import math

def test_all():
    def test_function(x: float) -> float:
        return (x + 2)*x*(x - 1)

    assert test_function(1) == 0
    assert test_function(0) == 0
    assert test_function(-2) == 0
    assert abs(grad(test_function)(0.549) - 0)  < 1e-2
    assert abs(grad(test_function)(-1.25) - 0)  < 0.2

    descent_problem = descent()

    gd = descent_problem.gradient_descent(test_function)
    nm = descent_problem.newtons_method(test_function)
    nmm = descent_problem.newtons_method_minimum(test_function)
    bfgs = descent_problem.BFGS(test_function)

    assert abs(gd - (0.55)) < 0.1
    assert abs(nm - (1)) < 0.1 or abs(nm - 0) < 0.1 or abs(nm - 2) < 0.1
    assert abs(nmm - (0.55)) < 0.1 or abs(nmm - (-1.25)) < 0.25 
    assert abs(bfgs - (0.55)) < 0.1 or abs(bfgs - (-1.25)) < 0.4

    results = descent_problem.run_all(test_function)
    assert results[0] == gd
    assert results[1] == nm
    assert results[2] == nmm
    assert results[3] == bfgs