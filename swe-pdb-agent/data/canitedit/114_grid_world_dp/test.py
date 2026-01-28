from solution import *
import math

def test_all():
    p1 = policy_str(policy)
    assert p1 == """TERM   | L      | L      | L      | L      | L      | L      | LD
U      | LU     | LU     | LU     | LU     | LU     | LRUD   | D
U      | LU     | LU     | LU     | LU     | LRUD   | RD     | D
U      | LU     | LU     | LU     | LRUD   | RD     | RD     | D
U      | LU     | LU     | LRUD   | RD     | RD     | RD     | D
U      | LU     | LRUD   | RD     | RD     | RD     | RD     | D
U      | LRUD   | RD     | RD     | RD     | RD     | RD     | D
RU     | R      | R      | R      | R      | R      | R      | TERM
"""
    p2 = init_policy()
    s2 = init_state_value()
    value_iteration(p2, s2, 10000)
    p2 = policy_str(p2)
    assert p2 == """TERM   | L      | LRUD   | LRUD   | LRUD   | LRUD   | LRUD   | LRUD
U      | LRUD   | LRUD   | LRUD   | LRUD   | LRUD   | LRUD   | LRUD
LRUD   | LRUD   | LRUD   | LRUD   | LRUD   | LRUD   | LRUD   | LRUD
LRUD   | LRUD   | LRUD   | LRUD   | LRUD   | LRUD   | LRUD   | LRUD
LRUD   | LRUD   | LRUD   | LRUD   | LRUD   | LRUD   | LRUD   | LRUD
LRUD   | LRUD   | LRUD   | LRUD   | LRUD   | LRUD   | LRUD   | LRUD
LRUD   | LRUD   | LRUD   | LRUD   | LRUD   | LRUD   | LRUD   | D
LRUD   | LRUD   | LRUD   | LRUD   | LRUD   | LRUD   | R      | TERM
"""
    p3 = init_policy()
    s3 = init_state_value()
    value_iteration(p3, s3, 1)
    p3 = policy_str(p3)
    assert p3 == """TERM   | L      | L      | L      | L      | L      | L      | LD
U      | LU     | LU     | LU     | LU     | LU     | LRUD   | D
U      | LU     | LU     | LU     | LU     | LRUD   | RD     | D
U      | LU     | LU     | LU     | LRUD   | RD     | RD     | D
U      | LU     | LU     | LRUD   | RD     | RD     | RD     | D
U      | LU     | LRUD   | RD     | RD     | RD     | RD     | D
U      | LRUD   | RD     | RD     | RD     | RD     | RD     | D
RU     | R      | R      | R      | R      | R      | R      | TERM
"""