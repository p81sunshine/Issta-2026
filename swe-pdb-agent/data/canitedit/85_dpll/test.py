from solution import *
import math

def test_all():
    input1 = 'A\n!A'
    assert DPLLSolver(input1).dpll() is None

    input2 = 'A'
    assert DPLLSolver(input2).dpll() == {'A': True}

    false_input = '!A'
    assert DPLLSolver(false_input).dpll() == {'A': False}

    false_double_input = '!A\nA'
    assert DPLLSolver(false_double_input).dpll() is None

    false_ab_input = '!A\n!B'
    assert DPLLSolver(false_ab_input).dpll() == {'A': False, 'B': False}

    empty_input = ''
    assert DPLLSolver(empty_input).dpll() == {}

    input3 = 'A\nB\n!A\n!B'
    assert DPLLSolver(input3).dpll() is None

    input4 = 'A\nB C\n!A !B\n!B !C'
    assert DPLLSolver(input4).dpll() == {'A': True, 'C': True, 'B': False}

    input5 = 'A B C\n!A !B\n!B !C\n!C !A'
    # in this case, only one literal can be True; all others must be False
    assert list(DPLLSolver(input5).dpll().values()).count(True) == 1

    solver = DPLLSolver('A B C')
    assert solver.assign_true == set()
    assert solver.assign_false == set()
    assert solver.n_props == 0
    assert solver.n_splits == 0
    assert solver.cnf == 'A B C'

    solver = DPLLSolver('A')
    assert solver.solve(['A'], ['A']) == True
    assert 'A' in solver.assign_true

    solver = DPLLSolver('A\n!A')
    assert solver.solve(['A', '!A'], ['A']) == False

    solver = DPLLSolver('A B')
    assert solver.solve(['A', 'B'], ['A', 'B']) == True
    assert 'A' in solver.assign_true and 'B' in solver.assign_true
    assert solver.n_props > 0
    assert solver.n_splits > 0

    assert DPLLSolver('A\n!A').dpll() is None
    assert DPLLSolver('A').dpll() == {'A': True}
    assert DPLLSolver('').dpll() == {}
    assert DPLLSolver('A\nB\n!A\n!B').dpll() is None
    assert DPLLSolver('A B\n!A !B\n!B !A').dpll() != None

    # mock the print function

    import builtins
    old_print = builtins.print
    builtins.print = lambda x: x

    # run print_cnf method
    DPLLSolver('A B\n!A !B\n!B !A').print_cnf()

    # restore the print function
    builtins.print = old_print

    assert DPLLSolver('A B C\n!A D E\n!B !D\n!C E').dpll(
    ) is not None  # should be satisfiable

    backtrack_input1 = 'A B\n!A C\n!B !C\nC'
    solver = DPLLSolver(backtrack_input1)
    assert solver.dpll() is not None  # should be satisfiable after backtracking
    # one of them should be backtracked
    assert 'A' in solver.assign_false or 'B' in solver.assign_false

    cnf1 = 'A\n!A B\n!B'
    solver1 = DPLLSolver(cnf1)
    assert solver1.dpll() is None
    assert solver1.assign_true == set(), "No assignments should remain after backtracking."
    assert solver1.assign_false == set(), "No assignments should remain after backtracking."

    cnf2 = 'A B\n!A C\n!B\n!C'
    solver2 = DPLLSolver(cnf2)
    assert solver2.dpll() is None
    assert solver2.assign_true == set(), "No assignments should remain after backtracking."
    assert solver2.assign_false == set(), "No assignments should remain after backtracking."

    cnf3 = 'A B\n!A C\n!B\n!C'
    solver3 = DPLLSolver(cnf3)
    assert solver3.dpll() is None
    assert solver3.assign_true == set(
    ), "No assignments should remain after backtracking."
    assert solver3.assign_false == set(
    ), "No assignments should remain after backtracking."

    solver = DPLLSolver('A\n!A B\n!B')
    assert not solver.solve(['A', '!A B', '!B'], [
                            'A', 'B'])
    assert 'A' not in solver.assign_true
    assert 'B' not in solver.assign_true

    solver = DPLLSolver('A B\n!A C\n!C\n!B')
    assert not solver.solve(['A B', '!A C', '!C', '!B'], [
                            'A', 'B', 'C'])
    assert 'A' not in solver.assign_true
    assert 'B' not in solver.assign_true
    assert 'C' not in solver.assign_true

    solver = DPLLSolver('A B\n!A C\n!C D\n!B D\n!D')
    assert not solver.solve(['A B', '!A C', '!C D', '!B D', '!D'], [
                            'A', 'B', 'C', 'D'])
    assert 'A' not in solver.assign_true
    assert 'B' not in solver.assign_true
    assert 'C' not in solver.assign_true
    assert 'D' not in solver.assign_true