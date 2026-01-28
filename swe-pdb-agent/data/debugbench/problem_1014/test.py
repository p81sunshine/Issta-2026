from solution import *

def test_example_1():
    persons = [0, 1, 1, 0, 0, 1, 0]
    times = [0, 5, 10, 15, 20, 25, 30]
    obj = TopVotedCandidate(persons, times)
    assert obj.q(3) == 0, "Failed at t=3"
    assert obj.q(12) == 1, "Failed at t=12"
    assert obj.q(25) == 1, "Failed at t=25"
    assert obj.q(15) == 0, "Failed at t=15"
    assert obj.q(24) == 0, "Failed at t=24"
    assert obj.q(8) == 1, "Failed at t=8"

def test_last_time():
    persons = [0, 1]
    times = [1, 2]
    obj = TopVotedCandidate(persons, times)
    assert obj.q(2) == 1, "Failed at last time"

def test_single_candidate():
    persons = [0]
    times = [5]
    obj = TopVotedCandidate(persons, times)
    assert obj.q(5) == 0, "Failed for single candidate"

def test_tie_case():
    persons = [0, 1, 0, 1]
    times = [1, 2, 3, 4]
    obj = TopVotedCandidate(persons, times)
    assert obj.q(2) == 1, "Tie case failed at t=2"
    assert obj.q(3) == 0, "Tie case failed at t=3"
    assert obj.q(4) == 1, "Tie case failed at t=4"