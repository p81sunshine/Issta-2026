from solution import *

import math

from solution import *

import math

from solution import *

import math

import numpy as np
def test_find_zero_base():
    result = find_zero([-10, -2])
    expected = -5.0
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=0.0001)
    result = find_zero([-3, -6, -7, 7])
    expected = 1.6679422344071086
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=0.0001)
    result = find_zero([8, 3])
    expected = -2.6666666666666665
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=0.0001)
    result = find_zero([-10, -8])
    expected = -1.25
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=0.0001)
    result = find_zero([-3, 6, 9, -10])
    expected = 0.3763741272657057
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=0.0001)
    result = find_zero([10, 7, 3, -3])
    expected = 2.481558752207975
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=0.0001)
    result = find_zero([8, -2, -10, -5, 3, 1, -2, -6])
    expected = 0.7057115511709099
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=0.0001)
    result = find_zero([1, -7, -8, 2])
    expected = 0.12543848593595794
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=0.0001)
    result = find_zero([1, 1])
    expected = -1.0
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=0.0001)
    result = find_zero([-9, 4, 7, -7, 2, -8])
    expected = -0.8164280553160108
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=0.0001)
    result = find_zero([10, 9, 1, 8, -4, -8])
    expected = -1.276698684687246
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=0.0001)
    result = find_zero([-3, -1])
    expected = -3.0
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=0.0001)
    result = find_zero([-3, -7])
    expected = -0.42857142857142855
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=0.0001)
    result = find_zero([-2, 4, 10, 1, -5, 1, 1, -4])
    expected = 0.2908351937976529
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=0.0001)
    result = find_zero([10, -8, 9, 10, -5, 7])
    expected = -1.07310389015689
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=0.0001)
    result = find_zero([-5, 4, 2, -2])
    expected = -1.4836825707186396
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=0.0001)
    result = find_zero([1, -9, -3, -9])
    expected = 0.10615823036409335
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=0.0001)
    result = find_zero([2, -2, -8, -4, 8, 1])
    expected = 1.1907846022361923
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=0.0001)
    result = find_zero([10, 5, 2, 10])
    expected = -0.8933423025111595
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=0.0001)
    result = find_zero([-6, -2, -6, -3, 7, 7, -2, 8])
    expected = 0.9600706108779886
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=0.0001)
    result = find_zero([8, 2, 1, -3, -6, 6, 5, -8])
    expected = 1.1312650071522643
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=0.0001)
    result = find_zero([-7, -6])
    expected = -1.1666666666666667
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=0.0001)
    result = find_zero([3, 9, -8, 2])
    expected = -0.26616881903379663
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=0.0001)
    result = find_zero([9, 4, 6, -2, 7, -10, -7, 7])
    expected = -1.2858021693375896
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=0.0001)
    result = find_zero([10, 1, -7, -1, 3, -5])
    expected = 1.0328693958196171
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=0.0001)
    result = find_zero([-10, -2, 6, -5, 6, -7, 10, -1])
    expected = -0.7015198788268473
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=0.0001)
    result = find_zero([-6, 1, -5, 7])
    expected = 1.1949840263103098
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=0.0001)
    result = find_zero([9, 1])
    expected = -9.0
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=0.0001)
    result = find_zero([-10, -7, 1, -1, -3, -9, -3, 8])
    expected = 1.5114667361718894
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=0.0001)
    result = find_zero([-8, 5])
    expected = 1.6
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=0.0001)
    result = find_zero([7, -6])
    expected = 1.1666666666666667
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=0.0001)
    result = find_zero([5, 7, -5, -2])
    expected = -0.5472144844465354
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=0.0001)
    result = find_zero([-4, 7, -4, -1, 2, 10, 1, 4])
    expected = 0.6221469265945829
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=0.0001)
    result = find_zero([-7, -3, -3, -8, 1, -10, 8, 7])
    expected = -2.004351767658384
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=0.0001)
    result = find_zero([8, -3, -10, -8])
    expected = 0.6355658373975246
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=0.0001)
    result = find_zero([-3, -8])
    expected = -0.375
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=0.0001)
    result = find_zero([1, -8])
    expected = 0.125
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=0.0001)
    result = find_zero([-2, 5, -4, 7])
    expected = 0.4360396215500477
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=0.0001)
    result = find_zero([8, 8, 5, -3])
    expected = 2.9021429109611363
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=0.0001)
    result = find_zero([3, -4, -7, -7, 3, 1, 3, 3])
    expected = 0.3945686794027269
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=0.0001)
    result = find_zero([-9, 10, 10, -7, -9, 2, 1, -7])
    expected = -1.0938426014292448
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=0.0001)
    result = find_zero([-4, -4, 7, 4])
    expected = -0.5930703238279362
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=0.0001)
    result = find_zero([3, -5, -2, 4])
    expected = 0.6513878134584461
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=0.0001)
    result = find_zero([-8, 4, 7, -7])
    expected = -0.9312933493196137
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=0.0001)
    result = find_zero([10, 7])
    expected = -1.4285714285714286
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=0.0001)
    result = find_zero([-8, -3])
    expected = -2.6666666666666665
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=0.0001)
    result = find_zero([3, 5, 5, -4])
    expected = 2.0420076280017767
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=0.0001)
    result = find_zero([-9, -5, 2, -10, 2, -2, 4, -1])
    expected = -0.6912828061190064
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=0.0001)
    result = find_zero([7, 5, -6, -4, -1, -4, -9, 8])
    expected = -0.7303538546846042
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=0.0001)
    result = find_zero([1, -9])
    expected = 0.1111111111111111
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=0.0001)
    result = find_zero([8, 5])
    expected = -1.6
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=0.0001)
    result = find_zero([-9, 6, -8, -5])
    expected = -2.408522928295524
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=0.0001)
    result = find_zero([9, -8])
    expected = 1.125
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=0.0001)
    result = find_zero([2, -7, 8, -3])
    expected = 0.6666666532827593
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=0.0001)
    result = find_zero([9, -8])
    expected = 1.125
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=0.0001)
    result = find_zero([8, 8, 6, 1, -2, -4, 1, -3])
    expected = 1.2670063990533957
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=0.0001)
    result = find_zero([2, -6, 10, -1, 4, 1])
    expected = -4.7214266139587755
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=0.0001)
    result = find_zero([-10, 4])
    expected = 2.5
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=0.0001)
    result = find_zero([-8, 7])
    expected = 1.1428571428571428
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=0.0001)
    result = find_zero([6, -2, -6, 1])
    expected = 0.9066403799501622
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=0.0001)
    result = find_zero([-3, 1])
    expected = 3.0
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=0.0001)
    result = find_zero([-5, 4, 7, -1, 9, 10])
    expected = 0.5266727586362528
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=0.0001)
    result = find_zero([7, -1])
    expected = 7.0
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=0.0001)
    result = find_zero([-6, -2])
    expected = -3.0
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=0.0001)
    result = find_zero([-7, 7])
    expected = 1.0
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=0.0001)
    result = find_zero([-2, -1, 9, -4])
    expected = -0.3903882210991383
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=0.0001)
    result = find_zero([-4, 10, -2, 6, 5, -2])
    expected = 0.3859218130812834
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=0.0001)
    result = find_zero([-8, 10])
    expected = 0.8
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=0.0001)
    result = find_zero([-2, -9, -10, 1, -6, 10, -2, -5])
    expected = -1.9016489783058546
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=0.0001)
    result = find_zero([7, 3, 7, -10, -7, -8, -6, 7])
    expected = -1.1438701575748802
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=0.0001)
    result = find_zero([1, 8])
    expected = -0.125
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=0.0001)
    result = find_zero([3, -6, -9, -1])
    expected = 0.3303230498267381
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=0.0001)
    result = find_zero([-9, 1, -4, -3, -7, 1])
    expected = 7.473522339226053
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=0.0001)
    result = find_zero([9, -6, -3, -5, -5, 3, -10, -5])
    expected = 0.6800906584848323
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=0.0001)
    result = find_zero([3, -3, -2, -5, -7, 2])
    expected = 0.5000000002574285
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=0.0001)
    result = find_zero([5, -3])
    expected = 1.6666666666666667
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=0.0001)
    result = find_zero([4, 1, -1, -3])
    expected = 1.091414272383764
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=0.0001)
    result = find_zero([-10, -4, 2, 1])
    expected = 2.1179422719613332
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=0.0001)
    result = find_zero([-8, -2, 1, 10, 6, 2])
    expected = 0.8199922739620269
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=0.0001)
    result = find_zero([-10, -7, -2, -5, 8, -2])
    expected = -0.7751167178723505
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=0.0001)
    result = find_zero([-7, 9])
    expected = 0.7777777777777778
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=0.0001)
    result = find_zero([1, 1, 3, 9, 6, -7, 2, 8])
    expected = -1.0796475563152408
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=0.0001)
    result = find_zero([-2, -9, 3, -10])
    expected = -0.2000001230542504
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=0.0001)
    result = find_zero([1, 3, -8, 1])
    expected = -0.21122096950972186
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=0.0001)
    result = find_zero([-7, -1, 6, -1, 3, 1])
    expected = -3.6929551973151455
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=0.0001)
    result = find_zero([-1, 7, -6, -4, 3, 2, -5, 9])
    expected = 0.1700721777911341
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=0.0001)
    result = find_zero([2, 7, -10, -1, -1, -4])
    expected = -0.2187870224956706
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=0.0001)
    result = find_zero([8, 9, 10, 1, 4, 4, 4, -4])
    expected = 2.0185353198764595
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=0.0001)
    result = find_zero([-5, -8, -1, 6, 10, 9, 1, -8])
    expected = -0.7318775289282917
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=0.0001)
    result = find_zero([-1, -3, -4, -6])
    expected = -0.4203806159365355
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=0.0001)
    result = find_zero([-9, -3])
    expected = -3.0
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=0.0001)
    result = find_zero([9, -8, 4, 3, 10, 8, -4, 2])
    expected = -1.2079210931679463
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=0.0001)
    result = find_zero([2, -3, -6, 10, -10, -7, 3, -3])
    expected = 0.4243726070846435
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=0.0001)
    result = find_zero([6, 4, -9, 7])
    expected = -0.5456791535804649
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=0.0001)
    result = find_zero([-7, 4, -6, 4])
    expected = 1.5720203886659294
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=0.0001)
    result = find_zero([4, 9, 6, 3, 7, 4])
    expected = -1.4282609139932105
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=0.0001)
    result = find_zero([5, 4, -2, -3])
    expected = 1.3137955382283977
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=0.0001)
    result = find_zero([6, 5, 10, -3, -2, 4])
    expected = -1.3557374680626677
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=0.0001)
    result = find_zero([-1, -3])
    expected = -0.3333333333333333
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=0.0001)
    result = find_zero([1, 1, 7, -8, -6, -6])
    expected = 0.6961120651027431
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=0.0001)
