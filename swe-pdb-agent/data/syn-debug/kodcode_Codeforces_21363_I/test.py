from solution import *

import math

from solution import *

import math

from solution import *

import math

def test_compute_max_photos_example():
    H, W = 5, 5
    n = 3
    photos = [(1, 2), (2, 2), (3, 3)]
    assert compute_max_photos(H, W, n, photos) == 3

def test_compute_max_photos_single_large_photo():
    H, W = 10, 10
    n = 1
    photos = [(10, 10)]
    assert compute_max_photos(H, W, n, photos) == 1

def test_compute_max_photos_no_photos_fit():
    H, W = 2, 2
    n = 3
    photos = [(3, 3), (4, 4), (5, 5)]
    assert compute_max_photos(H, W, n, photos) == 0

def test_compute_max_photos_multiple_small_photos():
    H, W = 3, 3
    n = 4
    photos = [(1, 1), (1, 1), (1, 1), (1, 1)]
    assert compute_max_photos(H, W, n, photos) == 4

def test_compute_max_photos_varied_photo_sizes():
    H, W = 6, 6
    n = 4
    photos = [(2, 2), (2, 2), (3, 3), (1, 1)]
    assert compute_max_photos(H, W, n, photos) == 4