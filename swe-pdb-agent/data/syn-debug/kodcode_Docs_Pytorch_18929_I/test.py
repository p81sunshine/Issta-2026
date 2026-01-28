from solution import *

import math

from solution import *

import math

from solution import *

import math

def test_custom_linear_forward():
    input = torch.randn(2, 3, dtype=torch.double)
    weight = torch.randn(3, 3, dtype=torch.double)
    bias = torch.randn(3, dtype=torch.double)

    output = CustomLinearFunction.apply(input, weight, bias)
    expected_output = input.mm(weight.t()) + bias
    assert torch.allclose(output, expected_output, atol=1e-6)

def test_custom_activation_forward():
    input = torch.randn(2, 3, dtype=torch.double)
    output = CustomActivationFunction.apply(input)
    expected_output = input ** 3
    assert torch.allclose(output, expected_output, atol=1e-6)

def test_custom_linear_backward():
    input = torch.randn(2, 3, dtype=torch.double, requires_grad=True)
    weight = torch.randn(3, 3, dtype=torch.double, requires_grad=True)
    bias = torch.randn(3, dtype=torch.double, requires_grad=True)
    
    output = CustomLinearFunction.apply(input, weight, bias)
    output.sum().backward()

    assert input.grad is not None
    assert weight.grad is not None
    assert bias.grad is not None

def test_custom_activation_backward():
    input = torch.randn(2, 3, dtype=torch.double, requires_grad=True)
    
    output = CustomActivationFunction.apply(input)
    output.sum().backward()

    assert input.grad is not None

def test_gradient_validation():
    assert validate_gradients() == True