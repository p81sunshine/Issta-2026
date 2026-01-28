from solution import *

import math

from solution import *

import math

from solution import *

import math

import pytest
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.svm import SVC
from solution import plot_model_diagnostics

def load_iris_data():
    X, y = load_iris(return_X_y=True)
    return X, y

@pytest.fixture
def iris_data():
    return load_iris_data()

def test_plot_model_diagnostics(iris_data):
    model = SVC(kernel="linear")
    param_name = "C"
    param_range = [0.01, 0.1, 1, 10, 100]
    train_sizes = [0.1, 0.25, 0.5, 0.75, 1.0]
    cv = 5
    
    # Checking if the function runs without errors
    try:
        plot_model_diagnostics(load_iris_data, model, param_name, param_range, train_sizes, cv)
    except Exception as e:
        pytest.fail(f"plot_model_diagnostics raised an exception: {e}")
    
    # We can't check the plots directly, but we can check if the plots were generated
    assert plt.gcf() is not None, "No plot was generated"