from solution import *

def test_example_1():
    persons = [0, 1, 1, 0, 0, 1, 0]
    times = [0, 5, 10, 15, 20, 25, 30]
    q = top_voted_candidate(persons, times)
    assert q(3) == 0, "q(3) should return 0"
    assert q(12) == 1, "q(12) should return 1"
    assert q(25) == 1, "q(25) should return 1"
    assert q(15) == 0, "q(15) should return 0"
    assert q(24) == 0, "q(24) should return 0"
    assert q(8) == 1, "q(8) should return 1"

def test_tie_case():
    persons = [0, 1]
    times = [1, 2]
    q = top_voted_candidate(persons, times)
    assert q(1) == 0, "At time 1, the leader should be 0 (tie resolved by most recent vote)"

def test_all_same_person():
    persons = [0, 0, 0]
    times = [1, 2, 3]
    q = top_voted_candidate(persons, times)
    assert q(1) == 0, "All votes for 0, q(1) should return 0"
    assert q(2) == 0, "All votes for 0, q(2) should return 0"
    assert q(3) == 0, "All votes for 0, q(3) should return 0"

def test_edge_time_at_time_point():
    persons = [0, 1]
    times = [1, 2]
    q = top_voted_candidate(persons, times)
    assert q(1) == 0, "At time exactly matching timestamp, should return previous leader"