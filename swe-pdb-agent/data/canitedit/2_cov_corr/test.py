from solution import *
import math

def test_all():
    X1 = [1.2, 3.5, 7.8, 4.6, 5.7, 8.9, 6.4, 10.2, 3.9, 7.1]
    X2 = [0.5, 2.3, 4.7, 6.9, 16.0, 18.2, 20.5, 22.7, 24.9]
    X3 = [2.75, 3.82, 5.16, 6.91, 9.24, 19.45, 21.18, 23.56, 25.99]
    X4 = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7]

    assert round(Probability().sample_mean(X1), 2) == 5.93
    assert round(Probability().sample_mean(X2), 2) == 12.97
    assert round(Probability().sample_mean(X3), 2) == 13.12
    assert round(Probability().sample_mean(X4), 2) == 0.40

    assert round(Probability().variance(X1), 2) == 6.64
    assert round(Probability().variance(X2), 2) == 78.31
    assert round(Probability().variance(X3), 2) == 76.74
    assert round(Probability().variance(X4), 2) == 0.04

    assert round(Probability().covariance(4, 7, 3)) == 18
    assert round(Probability().covariance(2, 10, 58)) == 48
    assert round(Probability().covariance(6, 8, 27)) == 88
    assert round(Probability().covariance(39, 2, 13)) == 199
    assert round(Probability().covariance(9, 3, 7)) == 41