from solution import *

import math

from solution import *

import math

from solution import *

import math

from solution import build_chain, generate_text

def test_build_chain_empty_text():
    assert build_chain("") == {}

def test_build_chain_single_character():
    assert build_chain("a") == {}

def test_build_chain_simple_text():
    chain = build_chain("hello")
    assert chain['h'] == {'e': 1.0}
    assert chain['e'] == {'l': 1.0}
    assert chain['l'] == {'l': 0.5, 'o': 0.5}
    assert chain['o'] == {}

def test_generate_text_simple():
    chain = build_chain("hello")
    text = generate_text(chain, 'h', 5)
    assert text[0] == 'h'
    assert len(text) == 5

def test_generate_text_with_edge_cases():
    chain = {'a': {'b': 1.0}, 'b': {'c': 1.0}, 'c': {'a': 1.0}}
    text = generate_text(chain, 'a', 6)
    assert text == "abcabc"  # cycle through the characters

def test_generate_text_with_unreachable_state():
    chain = {'a': {'b': 1.0}, 'b': {'a': 1.0}}
    text = generate_text(chain, 'b', 4)
    assert text == "baba" or text == "abab"  # both are valid cycles
    text = generate_text(chain, 'c', 4)
    assert text == "c"  # since 'c' isn't in the chain, it should just return 'c'

def test_generate_text_random_output():
    chain = build_chain("abacaba")
    generated_text = generate_text(chain, 'a', 7)
    assert len(generated_text) == 7  # the function should generate text of correct length
    assert generated_text[0] == 'a'  # starting character should be the initial character