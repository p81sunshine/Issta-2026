from solution import *
import math

def test_all():
    complex_ish = """
a = 1
b = 2
y, z = 3, 4
print(a + b)
print(y + z)

def f(x, arg=2):
    return x + a + arg
print(f(1))
print(f(2))
print(f(3))
"""

    parsed = ast.parse(complex_ish)
    uc = UsageCounter()
    uc.visit(parsed)
    assert uc.usages == {'a': 2, 'b': 1, 'y': 1,
                         'z': 1, 'x': 1, 'arg': 1, 'f': 3}

    simple_code = """
a = 1
b = 2
print(a)
"""
    parsed_simple = ast.parse(simple_code)
    uc_simple = UsageCounter()
    uc_simple.visit(parsed_simple)
    assert uc_simple.usages == {
        'a': 1, 'b': 0}

    assignment_code = """
a = 1
b = a + 2
c = a + b
"""
    parsed_assignment = ast.parse(assignment_code)
    uc_assignment = UsageCounter()
    uc_assignment.visit(parsed_assignment)
    assert uc_assignment.usages == {'a': 2, 'b': 1, 'c': 0}

    complex_code = """
def outer(x):
    y = x * 2
    def inner(z):
        return y + z
    return inner
"""
    parsed_complex = ast.parse(complex_code)
    uc_complex = UsageCounter()
    uc_complex.visit(parsed_complex)
    assert uc_complex.usages == {'x': 1, 'y': 1, 'z': 1, 'inner': 1, 'outer': 0}

    edge_case_code = """
a = 1
b = 2
a = b
c = a + b
"""
    parsed_edge_case = ast.parse(edge_case_code)
    uc_edge_case = UsageCounter()
    uc_edge_case.visit(parsed_edge_case)
    assert uc_edge_case.usages == {'a': 1, 'b': 2, 'c': 0}

    multiple_assignments_code = """
a, b = 0, 1
c = a + b
a, b = b, c
"""
    parsed_multiple_assignments = ast.parse(multiple_assignments_code)
    uc_multiple_assignments = UsageCounter()
    uc_multiple_assignments.visit(parsed_multiple_assignments)
    assert uc_multiple_assignments.usages == {'a': 1, 'b': 2, 'c': 1}

    global_local_code = """
x = 5
def f():
    x = 10
    return x
y = x
"""
    parsed_global_local = ast.parse(global_local_code)
    uc_global_local = UsageCounter()
    uc_global_local.visit(parsed_global_local)
    assert uc_global_local.usages == {'x': 2, 'y': 0, 'f': 0}

    loops_conditionals_code = """
i = 10
while i > 0:
    i -= 1
    if i == 5:
        break
"""
    parsed_loops_conditionals = ast.parse(loops_conditionals_code)
    uc_loops_conditionals = UsageCounter()
    uc_loops_conditionals.visit(parsed_loops_conditionals)
    assert uc_loops_conditionals.usages == {'i': 3}