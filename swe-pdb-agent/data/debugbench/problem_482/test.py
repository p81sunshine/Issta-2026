from solution import *

def test_example_1():
    top_voted = TopVotedCandidate([0, 1, 1, 0, 0, 1, 0], [0, 5, 10, 15, 20, 25, 30])
    assert top_voted.q(3) == 0, "Failed for t=3: should return leading candidate at time 3"

def test_example_2():
    top_voted = TopVotedCandidate([0, 1, 1, 0, 0, 1, 0], [0, 5, 10, 15, 20, 25, 30])
    assert top_voted.q(24) == 0, "Failed for t=24: should return leading candidate at time 24"

def test_example_3():
    top_voted = TopVotedCandidate([0, 1, 1, 0, 0, 1, 0], [0, 5, 10, 15, 20, 25, 30])
    assert top_voted.q(25) == 1, "Failed for t=25: should return leading candidate at time 25"

def test_edge_case_t0():
    top_voted = TopVotedCandidate([0, 1, 1, 0, 0, 1, 0], [0, 5, 10, 15, 20, 25, 30])
    assert top_voted.q(0) == 0, "Failed for t=0: should return initial candidate at time 0"