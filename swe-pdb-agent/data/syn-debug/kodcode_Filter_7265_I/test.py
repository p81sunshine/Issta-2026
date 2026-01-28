from solution import *

import math

from solution import *

import math

from solution import *

import math

import pytest
from solution import Lexer, Parser

def test_number_expression():
    lexer = Lexer('42')
    parser = Parser(lexer)
    tree = parser.parse()
    assert tree.value == 42

def test_addition():
    lexer = Lexer('1 + 2')
    parser = Parser(lexer)
    tree = parser.parse()
    assert tree[0].type == 'ADD'
    assert tree[1].value == 1
    assert tree[2].value == 2

def test_subtraction():
    lexer = Lexer('5 - 3')
    parser = Parser(lexer)
    tree = parser.parse()
    assert tree[0].type == 'SUB'
    assert tree[1].value == 5
    assert tree[2].value == 3

def test_multiplication():
    lexer = Lexer('4 * 3')
    parser = Parser(lexer)
    tree = parser.parse()
    assert tree[0].type == 'MUL'
    assert tree[1].value == 4
    assert tree[2].value == 3

def test_division():
    lexer = Lexer('8 / 2')
    parser = Parser(lexer)
    tree = parser.parse()
    assert tree[0].type == 'DIV'
    assert tree[1].value == 8
    assert tree[2].value == 2

def test_combined_expression():
    lexer = Lexer('3 + 2 * (1 + 5)')
    parser = Parser(lexer)
    tree = parser.parse()
    assert tree[0].type == 'ADD'
    assert tree[1].value == 3
    assert tree[2][0].type == 'MUL'
    assert tree[2][1].value == 2
    assert tree[2][2][0].type == 'ADD'
    assert tree[2][2][1].value == 1
    assert tree[2][2][2].value == 5