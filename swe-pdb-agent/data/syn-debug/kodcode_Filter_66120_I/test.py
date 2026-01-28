from solution import *

import math

from solution import *

import math

from solution import *

import math

import pytest
import numpy as np
from solution import SimpleNeuralNetwork

def test_feedforward():
    nn = SimpleNeuralNetwork(input_size=2, hidden_layer_size=3, output_size=1)
    X = np.array([[0, 0], [1, 1]])
    output = nn.feedforward(X)
    assert output.shape == (2, 1)

def test_backpropagate():
    nn = SimpleNeuralNetwork(input_size=2, hidden_layer_size=3, output_size=1)
    X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    y = np.array([[0], [1], [1], [0]])
    initial_weights_input_hidden = nn.weights_input_hidden.copy()
    initial_weights_hidden_output = nn.weights_hidden_output.copy()
    
    nn.backpropagate(X, y, learning_rate=0.1)
    
    assert not np.array_equal(nn.weights_input_hidden, initial_weights_input_hidden)
    assert not np.array_equal(nn.weights_hidden_output, initial_weights_hidden_output)

def test_train():
    nn = SimpleNeuralNetwork(input_size=2, hidden_layer_size=3, output_size=1)
    X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    y = np.array([[0], [1], [1], [0]])
    nn.train(X, y, epochs=1000, learning_rate=0.1)
    predictions = nn.predict(X)
    
    assert predictions.shape == (4, 1)
    assert all(0 <= pred <= 1 for pred in predictions.flatten())

def test_predict():
    nn = SimpleNeuralNetwork(input_size=2, hidden_layer_size=3, output_size=1)
    X = np.array([[0, 1], [1, 0]])
    predictions = nn.predict(X)
    
    assert predictions.shape == (2, 1)
    assert all(0 <= pred <= 1 for pred in predictions.flatten())