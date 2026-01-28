from solution import *

import math

from solution import *

import math

from solution import *

import math

import torch
import torch.nn as nn
from solution import CustomAttention, SimpleModel

def test_attention_layer():
    input_dim = 32
    attention_dim = 16
    output_dim = 32
    batch_size = 5
    sequence_length = 7

    x = torch.randn(batch_size, sequence_length, input_dim)
    attention = CustomAttention(input_dim, attention_dim, output_dim)

    output = attention(x)
    assert output.shape == (batch_size, sequence_length, output_dim)

def test_model_initialization():
    input_dim = 32
    attention_dim = 16
    output_dim = 32

    model = SimpleModel(input_dim, attention_dim, output_dim)
    assert isinstance(model, nn.Module)

def test_model_forward_pass():
    input_dim = 32
    attention_dim = 16
    output_dim = 32
    batch_size = 5
    sequence_length = 7

    model = SimpleModel(input_dim, attention_dim, output_dim)
    x = torch.randn(batch_size, sequence_length, input_dim)

    output = model(x)
    assert output.shape == (batch_size, sequence_length, output_dim)

def test_training_step():
    input_dim = 32
    attention_dim = 16
    output_dim = 32
    x_train = torch.randn(100, 10, input_dim)
    y_train = torch.randn(100, 10, output_dim)

    model = SimpleModel(input_dim, attention_dim, output_dim)
    criterion = nn.MSELoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

    optimizer.zero_grad()
    output = model(x_train)
    loss = criterion(output, y_train)
    loss.backward()
    optimizer.step()

    assert loss.item() > 0

if __name__ == '__main__':
    test_attention_layer()
    test_model_initialization()
    test_model_forward_pass()
    test_training_step()
    print("All tests passed successfully!")