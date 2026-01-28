from solution import *

import math

from solution import *

import math

from solution import *

import math

import pytest
from solution import impute_and_evaluate

@pytest.fixture
def create_dummy_csv(tmp_path):
    data = """Feature1,Feature2,Feature3,Target
1.0,2.0,A,0
2.0,NaN,B,1
NaN,5.0,A,0
4.0,5.0,B,1
5.0,NaN,A,0
NaN,10.0,B,1"""
    data_file = tmp_path / "data.csv"
    data_file.write_text(data)
    return data_file

def test_simple_imputer(create_dummy_csv):
    accuracy = impute_and_evaluate('simple', create_dummy_csv)
    assert accuracy >= 0.0 and accuracy <= 1.0

def test_iterative_imputer(create_dummy_csv):
    accuracy = impute_and_evaluate('iterative', create_dummy_csv)
    assert accuracy >= 0.0 and accuracy <= 1.0

def test_knn_imputer(create_dummy_csv):
    accuracy = impute_and_evaluate('knn', create_dummy_csv)
    assert accuracy >= 0.0 and accuracy <= 1.0

def test_invalid_imputer_method(create_dummy_csv):
    with pytest.raises(ValueError):
        impute_and_evaluate('unknown', create_dummy_csv)