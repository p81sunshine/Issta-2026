from solution import *
import math

def test_all():
    def acceptsString(dfa: DFA, word: List[Input]) -> bool:
        for symbol in word:
            dfa.current = dfa.transition(symbol)
        return dfa.accepted()

    assert acceptsString(DFA(), ["", "", "", "a"])
    assert acceptsString(DFA(), ["", "", "a"])
    assert acceptsString(DFA(), ["", "a"])
    assert acceptsString(DFA(), ["", "a", "b"])
    assert acceptsString(DFA(), ["", "a", "b", "", "", "b"])
    assert acceptsString(DFA(), ["", "a", "b", "", "", ""])
    assert acceptsString(DFA(), ["", "a", "b", "", "b", "", "b"])
    assert acceptsString(DFA(), ["", "a", "b", "b", "b"])
    assert acceptsString(DFA(), ["", "a", "b", "b"])

    assert not acceptsString(DFA(), ["b"])
    assert not acceptsString(DFA(), [""])
    assert not acceptsString(DFA(), ["a", "b", "a"])
    assert not acceptsString(DFA(), ["", "b"])
    assert not acceptsString(DFA(), ["", "", "b", "b"])
    assert not acceptsString(DFA(), ["", "a", "b", "b", "b", "a"])