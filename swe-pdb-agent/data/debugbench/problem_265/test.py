from solution import *

def test_example_1():
    persons = [0, 1, 1, 0, 0, 1, 0]
    times = [0, 5, 10, 15, 20, 25, 30]
    tv = TopVotedCandidate(persons, times)
    assert tv.q(3) == 0, "Failed at t=3"
    assert tv.q(12) == 1, "Failed at t=12"
    assert tv.q(25) == 1, "Failed at t=25"
    assert tv.q(15) == 0, "Failed at t=15"
    assert tv.q(24) == 0, "Failed at t=24"
    assert tv.q(8) == 1, "Failed at t=8"

def test_edge_case_out_of_bounds():
    persons = [0]
    times = [5]
    tv = TopVotedCandidate(persons, times)
    assert tv.q(10) == 0, "Should handle t greater than all times"

def test_tie_case():
    persons = [0, 1]
    times = [1, 1]
    tv = TopVotedCandidate(persons, times)
    assert tv.q(1) == 1, "Should return the most recent in case of tie"

def test_single_candidate():
    tv = TopVotedCandidate([42], [0])
    assert tv.q(0) == 42, "Should return the single candidate at exact time"