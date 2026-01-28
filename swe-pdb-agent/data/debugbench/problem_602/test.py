from solution import *

def test_example_1():
    persons = [0, 1, 1, 0, 0, 1, 0]
    times = [0, 5, 10, 15, 20, 25, 30]
    tv = TopVotedCandidate(persons, times)
    assert tv.q(3) == 0, "t=3 should return 0"
    assert tv.q(12) == 1, "t=12 should return 1"
    assert tv.q(25) == 1, "t=25 should return 1"
    assert tv.q(15) == 0, "t=15 should return 0"
    assert tv.q(24) == 0, "t=24 should return 0"
    assert tv.q(8) == 1, "t=8 should return 1"

def test_between_two_times():
    persons = [0, 1]
    times = [5, 10]
    tv = TopVotedCandidate(persons, times)
    assert tv.q(7) == 0, "At t=7 between 5 and 10, leader is 0"

def test_time_at_middle():
    persons = [0, 1]
    times = [10, 20]
    tv = TopVotedCandidate(persons, times)
    assert tv.q(10) == 0, "At t=10, leader is 0"

def test_time_exceeds_max():
    persons = [0]
    times = [5]
    tv = TopVotedCandidate(persons, times)
    assert tv.q(5) == 0, "t equals max time should return 0"

def test_tie_resolution():
    persons = [0, 1, 1]
    times = [0, 1, 2]
    tv = TopVotedCandidate(persons, times)
    # After first vote: [0]
    # After second vote: [0,1] (tie, but most recent vote wins)
    # After third vote: [0,1,1]
    assert tv.q(0) == 0
    assert tv.q(1) == 1
    assert tv.q(2) == 1