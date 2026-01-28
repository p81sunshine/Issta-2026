from solution import *

def test_example_1():
    tv = TopVotedCandidate([0, 1, 1, 0, 0, 1, 0], [0, 5, 10, 15, 20, 25, 30])
    assert tv.q(3) == 0, "q(3) should return 0"
    assert tv.q(12) == 1, "q(12) should return 1"
    assert tv.q(25) == 1, "q(25) should return 1"
    assert tv.q(15) == 0, "q(15) should return 0"
    assert tv.q(24) == 0, "q(24) should return 0"
    assert tv.q(8) == 1, "q(8) should return 1"

def test_tie_case():
    tv = TopVotedCandidate([0, 1], [1, 2])
    assert tv.q(2) == 1, "Tie should return the most recent voter"

def test_single_candidate():
    tv = TopVotedCandidate([5], [10])
    assert tv.q(10) == 5, "Single candidate should return that candidate"

def test_no_leader_change():
    tv = TopVotedCandidate([0, 0, 1], [1, 2, 3])
    assert tv.q(3) == 0, "Leader should remain 0 despite new vote for 1"