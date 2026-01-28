from solution import *

import math

from solution import *

import math

from solution import *

import math

from solution import suggest_songs

def test_suggest_songs_preferred_genre():
    n = 5
    songs = [(1, 3, 50), (2, 1, 70), (3, 3, 40), (4, 2, 60), (5, 3, 90)]
    x = 3
    y = 3
    k = 2
    assert suggest_songs(n, songs, x, y, k) == [5, 1]
    
def test_suggest_songs_different_genre():
    n = 5
    songs = [(1, 3, 50), (2, 1, 70), (3, 3, 40), (4, 2, 60), (5, 3, 90)]
    x = 3
    y = 1
    k = 2
    assert suggest_songs(n, songs, x, y, k) == [2, 4]
    
def test_suggest_songs_not_enough_preferred_or_other_genre():
    n = 6
    songs = [(1, 2, 50), (2, 2, 40), (3, 2, 30), (4, 3, 60), (5, 4, 90), (6, 4, 80)]
    x = 1
    y = 3
    k = 3
    assert suggest_songs(n, songs, x, y, k) == [4, 5, 6]

def test_no_suggestion_possible():
    n = 3
    songs = [(1, 2, 50), (2, 2, 40), (3, 2, 30)]
    x = 1
    y = 3
    k = 2
    assert suggest_songs(n, songs, x, y, k) == -1

def test_some_suggestions():
    n = 4
    songs = [(1, 1, 100), (2, 2, 50), (3, 1, 90), (4, 2, 80)]
    x = 1
    y = 2
    k = 2
    assert suggest_songs(n, songs, x, y, k) == [4, 2]