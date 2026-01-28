from solution import *

import math

from solution import *

import math

from solution import *

import math

from solution import get_accuracies

def test_accuracies_exist():
    accuracies = get_accuracies()
    assert "No Feature Selection" in accuracies
    assert "Variance Threshold" in accuracies
    assert "SelectKBest" in accuracies
    assert "RFE" in accuracies
    assert "Tree-based" in accuracies

def test_accuracies_are_floats():
    accuracies = get_accuracies()
    for key in accuracies:
        assert isinstance(accuracies[key], float)

def test_accuracies_not_zero():
    accuracies = get_accuracies()
    for key in accuracies:
        assert accuracies[key] > 0