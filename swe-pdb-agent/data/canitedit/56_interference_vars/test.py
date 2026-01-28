from solution import *
import math

def test_all():
    n = ALet("n",
             value=CImmExpr(ImmExpr(1, "int")),
             body=ALet("f",
                       value=CPrim("+", ImmExpr(1, "int"), ImmExpr("n", "id")),
                       body=ACExpr(CImmExpr(ImmExpr("f", "id")))))
    assert n.interfere(set(), set()) == {'n': {'f'}, 'f': {'n'}}
    imm_expr_id = ImmExpr("x", "id")
    assert imm_expr_id.free_vars() == {
        "x"}, "Failed: ImmExpr free_vars with identifier"

    imm_expr_int = ImmExpr(42, "int")
    assert imm_expr_int.free_vars() == set(), "Failed: ImmExpr free_vars with integer"

    c_if = CIf(ImmExpr("x", "id"), ACExpr(CImmExpr(
        ImmExpr("y", "id"))), ACExpr(CImmExpr(ImmExpr("z", "id"))))
    assert c_if.free_vars() == {"x", "y", "z"}, "Failed: CIf free_vars"
    assert c_if.interfere(set(), set()) == {}
    c_prim = CPrim("+", ImmExpr("a", "id"), ImmExpr("b", "id"))
    assert c_prim.interfere(set(), set()) == {}
    assert c_prim.free_vars() == {"a", "b"}, "Failed: CPrim free_vars"
    c_app = CApp(ImmExpr("f", "id"), [ImmExpr("a", "id"), ImmExpr("b", "id")])
    assert c_app.interfere(set(), set()) == {}
    assert c_app.free_vars() == {"f", "a", "b"}, "Failed: CApp free_vars"
    c_app = CApp(ImmExpr("f", "id"), [ImmExpr("a", "id"), ImmExpr("b", "id")])
    assert c_app.interfere(set(), set()) == {}
    assert c_app.free_vars() == {"f", "a", "b"}, "Failed: CApp free_vars"
    c_lambda = CLambda(["a", "b"], ACExpr(CImmExpr(ImmExpr("a", "id"))))
    assert c_lambda.interfere(set("a"), set()) == {}
    assert c_lambda.interfere(set(), set()) == {}
    assert c_lambda.free_vars() == set(), "Failed: CLambda free_vars"
    a_let = ALet("x", CImmExpr(ImmExpr("y", "id")),
                 ACExpr(CImmExpr(ImmExpr("x", "id"))))
    assert a_let.interfere(set(), set()) == {'x': {'y'}, 'y': {'x'}}
    assert a_let.free_vars() == {"y"}, "Failed: ALet free_vars"
    a_seq = ASeq(CImmExpr(ImmExpr("x", "id")),
                 ACExpr(CImmExpr(ImmExpr("y", "id"))))
    assert a_seq.interfere(set(), set()) == {}
    assert a_seq.free_vars() == {"x", "y"}, "Failed: ASeq free_vars"
    a_cexpr = ACExpr(CImmExpr(ImmExpr("x", "id")))
    assert a_cexpr.interfere(set(), set()) == {}
    assert a_cexpr.free_vars() == {"x"}, "Failed: ACExpr free_vars"
    c_lambda_c_app = CApp(ImmExpr("f", "id"), [
                          ImmExpr("a", "id"), ImmExpr("b", "id")])
    c_lambda_c_app = CLambda(["a", "b"], ACExpr(c_lambda_c_app))
    assert c_lambda_c_app.interfere(set(), set()) == {}
    assert c_lambda_c_app.free_vars() == {"f"}, "Failed: CLambda free_vars"
    a_let_c_lambda_c_app = ALet("f", c_lambda_c_app, ACExpr(
        CImmExpr(ImmExpr("f", "id"))))
    assert a_let_c_lambda_c_app.interfere(set("x"), set()) == {
        'f': {'x', 'f'}, 'x': {'f'}}
    assert a_let_c_lambda_c_app.free_vars() == {"f"}, "Failed: ALet free_vars"
    a_let_c_lambda_c_app_seq = ASeq(CImmExpr(ImmExpr("x", "id")),
                                    a_let_c_lambda_c_app)
    assert a_let_c_lambda_c_app_seq.interfere(set("x"), set()) == {
        'f': {'x', 'f'}, 'x': {'f'}}
    assert a_let_c_lambda_c_app_seq.free_vars(
    ) == {"x", "f"}, "Failed: ASeq free_vars"
    # another lambda with different parameters
    c_lambda_c_app = CApp(ImmExpr("g", "id"), [
                          ImmExpr("a", "id"), ImmExpr("b", "id")])
    c_lambda_c_app = CLambda(["a", "b"], ACExpr(c_lambda_c_app))
    c_lambda_c_app_let = ALet("g", c_lambda_c_app, ACExpr(
        CImmExpr(ImmExpr("g", "id"))))
    assert c_lambda_c_app_let.interfere(set("z"), set()) == {
        'g': {'z', 'g'}, 'z': {'g'}}
    assert c_lambda_c_app.interfere(set(), set()) == {}
    a_let_c_lambda_c_app_seq_c_if = CIf(ImmExpr("x", "id"), a_let_c_lambda_c_app_seq,
                                        c_lambda_c_app_let)
    assert a_let_c_lambda_c_app_seq_c_if.interfere(set("y"), set()) == {
        'f': {'y', 'f'}, 'y': {'f', 'g'}, 'g': {'y', 'g'}}, "Failed: CIf interfere"
    assert a_let_c_lambda_c_app_seq_c_if.free_vars(
    ) == {"g", "x", "f"}, "Failed: CIf free_vars"
    a_aseq = ASeq(CImmExpr(ImmExpr("x", "id")), ACExpr(
        CImmExpr(ImmExpr("y", "id"))))
    a_aseq_let = ALet("x", CImmExpr(ImmExpr("y", "id")), a_aseq)
    assert a_aseq_let.interfere(set("x"), set()) == {
        'x': {'y', 'x'}, 'y': {'x'}}, "Failed: ALet interfere"
    assert a_aseq_let.free_vars() == {"y"}, "Failed: ALet free_vars"
    a_aseq_let_c_lambda_c_app = ALet("f", c_lambda_c_app, a_aseq_let)
    assert a_aseq_let_c_lambda_c_app.interfere(set("k"), set()) == {'f': {'x', 'g', 'y', 'k'}, 'k': {
        'f', 'x'}, 'y': {'f', 'x'}, 'g': {'f'}, 'x': {'f', 'y', 'k'}}, "Failed: ALet interfere"
    assert a_aseq_let_c_lambda_c_app.interfere(set("k"), set("y")) == {'f': {'k', 'x', 'g'}, 'k': {
        'x', 'f'}, 'g': {'f'}, 'x': {'k', 'f'}}, "Failed: ALet interfere"