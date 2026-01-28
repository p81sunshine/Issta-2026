from solution import *

def test_example_1():
    top_voted = TopVotedCandidate([0, 1, 1, 0, 0, 1, 0], [0, 5, 10, 15, 20, 25, 30])
    assert top_voted.q(3) == 0
    assert top_voted.q(12) == 1
    assert top_voted.q(25) == 1
    assert top_voted.q(15) == 0
    assert top_voted.q(24) == 0
    assert top_voted.q(8) == 1

def test_before_first_time():
    top_voted = TopVotedCandidate([0], [5])
    assert top_voted.q(3) == 0, "Should return leader of the first time for t before earliest time"

def test_tie_case():
    top_voted = TopVotedCandidate([0, 1], [1, 2])
    assert top_voted.q(1) == 0, "At time=1, leader is 0"
    assert top_voted.q(2) == 1, "At time=2, leader is 1 (tie resolved by most recent)"

def test_same_leader():
    top_voted = TopVotedCandidate([0, 0, 0], [1, 2, 3])
    assert top_voted.q(0) == 0, "t before first time returns leader of first time"
    assert top_voted.q(1) == 0, "t equals first time"
    assert top_voted.q(2) == 0, "t equals second time"
    assert top_voted.q(4) == 0, "t after last time"