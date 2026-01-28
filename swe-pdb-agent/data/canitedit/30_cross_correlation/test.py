from solution import *
import math

import numpy as np
import torch
import torch.nn.functional as F

def test_all():
    im_size, ker_size, padding = 6, 3, 3

    im_sizes = [5, 10, 8]
    ker_sizes = [3, 2, 4]
    paddings = [0, 2, 3]

    for im_size, ker_size, pad in zip(im_sizes, ker_sizes, paddings):

        image = np.random.rand(im_size, im_size)
        kernel = np.random.rand(ker_size, ker_size) 

        expected = F.conv2d(torch.tensor(image).reshape(1, 1, im_size, im_size), torch.tensor(kernel).reshape(1, 1, ker_size, ker_size), padding=pad)
        actual = torch.tensor(cross_correlation(image, kernel, pad))
        assert torch.all(torch.abs(expected - actual) < 0.001) == True