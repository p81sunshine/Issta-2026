from solution import *

import math

from solution import *

import math

from solution import *

import math

from solution import build_graph_from_letters, valid_words, is_valid_word

def test_is_valid_word():
    assert is_valid_word('cat') == True
    assert is_valid_word('dog') == False

def test_generate_combinations():
    letters = 'cartd'
    words = generate_combinations(letters)
    for word in valid_words.intersection(words):
        assert word in valid_words

def test_build_graph_from_letters():
    letters = 'cart'
    graph = build_graph_from_letters(letters)
    
    nodes = set(graph.nodes)
    assert 'cat' in nodes
    assert 'cart' in nodes
    assert 'rat' in nodes
    assert 'bat' not in nodes
    
    assert graph.has_edge('cat', 'cart')
    assert not graph.has_edge('cat', 'bat')

def test_neighbors_function():
    assert are_neighbors('cat', 'bat') == True
    assert are_neighbors('cart', 'dart') == True
    assert are_neighbors('cat', 'dog') == False
    assert are_neighbors('cat', 'cats') == True
    assert are_neighbors('cat', 'rat') == True
    assert are_neighbors('cat', 'trace') == False