from solution import *
import math

def test_all():
    assert Number(1).eval({}) == 1
    assert BinOp(Number(1), "+", Number(2)).eval({}) == 3
    assert BinOp(Number(1), "-", Number(2)).eval({}) == -1
    assert BinOp(Number(1), "*", Number(2)).eval({}) == 2
    assert BinOp(Number(30), "*", Number(2)).eval({}) == 60
    assert BinOp(Number(30), "*", Number(-30)).eval({}) == -900
    assert BinOp(Number(-31), "*", Number(-99)).eval({}) == 3069
    assert BinOp(Number(1), "/", Number(2)).eval({}) == 0
    assert BinOp(Number(2), "/", Number(1)).eval({}) == 2
    assert BinOp(Number(2), "/", Number(3)).eval({}) == 0
    assert BinOp(Number(5), "/", Number(2)).eval({}) == 2
    assert BinOp(Number(5), "/", Number(3)).eval({}) == 1
    assert BinOp(Number(20), "/", Number(3)).eval({}) == 6
    assert BinOp(Number(20), "/", Number(5)).eval({}) == 4
    try:
        BinOp(Number(1), "/", Number(0)).eval({})
        assert False
    except ZeroDivisionError:
        pass
    assert Var("x", Number(1), BinOp(Name("x"), "+", Number(2))).eval({}) == 3
    assert Var("x", Number(1), BinOp(
        Name("y"), "+", Number(2))).eval({"y": 3}) == 5
    assert Var("x", Number(1), BinOp(Name("x"), "+", Name("x"))).eval({}) == 2
    assert Var("x", Number(1), BinOp(
        Name("x"), "+", Name("y"))).eval({"y": 3}) == 4
    assert Var("x", Number(1), BinOp(
        Name("y"), "+", Name("x"))).eval({"y": 3}) == 4
    assert Var("x", Number(1), BinOp(
        Name("y"), "+", Name("y"))).eval({"y": 3}) == 6
    assert Var("x", Number(1), BinOp(Name("x"), "+",
               BinOp(Name("x"), "+", Name("x")))).eval({}) == 3
    assert Var("x", Number(1), BinOp(Name("x"), "+",
               BinOp(Name("x"), "+", Name("y")))).eval({"y": 3}) == 5
    assert Var("x", Number(1), BinOp(Name("x"), "+",
               BinOp(Name("y"), "+", Name("x")))).eval({"y": 3}) == 5
    assert Var("x", Number(1), BinOp(Name("x"), "+",
               BinOp(Name("y"), "+", Name("y")))).eval({"y": 3}) == 7
    assert Var("x", Number(1), BinOp(Name("y"), "+",
               BinOp(Name("x"), "+", Name("x")))).eval({"y": 3}) == 5
    assert Var("x", Number(1), BinOp(Name("y"), "+",
               BinOp(Name("x"), "+", Name("y")))).eval({"y": 3}) == 7
    assert Var("x", Number(1), BinOp(Name("y"), "+",
                                     BinOp(Name("y"), "+", Name("x")))).eval({"y": 3}) == 7
    assert Var("x", Number(1), BinOp(Name("y"), "+",
                                     BinOp(Name("y"), "+", Name("y")))).eval({"y": 3}) == 9

    try:
        Name("blabla").eval({})
        assert False, "Should not be able to evaluate a variable that is not defined"
    except ValueError:
        pass

    try:
        BinOp(Number(1), "//", Number(2)).eval({})
        assert False, "Should not implement // operator"
    except ValueError:
        pass