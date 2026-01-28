from solution import *
import math

def test_all():
    p1 = 106370619031455416265556180880535612754694154891931768764891927199982044991293
    g1 = 62396934948727367902534680978401865344491133099510338373553753384248885001077
    x1 = 17293013998955379273582941822693540654895591849320486454120541612393742535976
    r1 = 24028398142591543250806503193994542025330165417040028048437578489502706200899
    c1 = 58462142818219555696526575106627315408589723652667386542863336101775663461338
    assert schnorr_protocol(p1,g1,x1,r1,c1)

    p2 = 11
    g2 = 3
    x2 = 5
    r2 = 7
    c2 = 2
    assert keygen(p2,g2,x2) == ((11,3,1),5)
    assert prover_commitment(p2,g2,r2) == (9,7)
    assert verifier_challenge(c2) == 2
    assert hash_to_challenge(9,1,11) == 0
    assert prover_response(7,c2,x2,p2) == 7
    assert verifier_check(p2,g2,1,9,c2,7)
    assert schnorr_protocol(p2,g2,x2,r2,c2)

    p3 = 439
    g3 = 100
    x3 = 200
    r3 = 300
    c3 = 400
    assert hash_to_challenge(16,237,439) == 135
    assert schnorr_protocol(p3,g3,x3,r3,c3)
    assert schnorr_protocol(0, 0, 0, 0, 0) == False