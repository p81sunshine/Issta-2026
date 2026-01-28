from solution import *
import math

def test_all():
    b1 = '''bleh
bleh'''
    a1 = '''bob
bleh
bleh'''

    b2 = '''hello
hello'''
    a2 = '''hello
hey
hello'''

    b3 = '''replacethis
hey'''
    a3 = '''replaced
hey'''

    b4 = '''lots
of
stuff'''
    a4 = ''''''

    b5 = '''only
one
thing
to
delete'''

    a5 = '''only
one
thing
to'''

    b6 = '''lol
lol'''
    a6 = '''before
lol'''

    b7 = '''lol
lol'''
    a7 = '''lol
bleh
lol'''

    b8 = '''missing
first'''
    a8 = '''word
missing
first'''

    b9 = '''two
inserts'''
    a9 = '''two
here
inserts
here'''

    b10 = '''two
here
dels
here'''
    a10 = '''two
dels'''

    assert create_rel_diff(b1, a1) == "0<add>bob"
    assert create_rel_diff(b2, a2) == "1<add>hey"
    assert create_rel_diff(b3, a3) == "1<del><add>replaced"
    assert create_rel_diff(b4, a4) == "1<del><add>\n2<del>\n3<del>"
    assert create_rel_diff(b5, a5) == "5<del>"
    assert create_rel_diff(b6, a6) == "1<del><add>before"
    assert create_rel_diff(b7, a7) == "1<add>bleh"
    assert create_rel_diff(b8, a8) == "0<add>word"
    assert create_rel_diff(b9, a9) == "1<add>here\n2<add>here"
    assert create_rel_diff(b10, a10) == "2<del>\n4<del>"

    assert create_syntax(["a", "b", "c"], 1) == "1<del><add>a\n1<add>b\n1<add>c\n"