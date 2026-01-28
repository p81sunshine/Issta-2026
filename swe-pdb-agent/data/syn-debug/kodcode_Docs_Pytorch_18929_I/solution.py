import torch
from torch.autograd import Function
import math

class CustomLinearFunction(Function):
    @staticmethod
    def forward(ctx, input, weight, bias=None):
        ctx.save_for_backward(input, weight, bias)
        output = input.mm(weight.t())
        if bias is not None:
            output += bias
        return output

    @staticmethod
    def backward(ctx, grad_output):
        input, weight, bias = ctx.saved_tensors
        grad_input = grad_weight = grad_bias = None

        if ctx.needs_input_grad[0]:
            grad_input = grad_output.mm(weight)
        if ctx.needs_input_grad[1]:
            grad_weight = grad_output.t().mm(input)
        if bias is not None and ctx.needs_input_grad[2]:
            grad_bias = grad_output.sum(0)

        return grad_input, grad_weight, grad_bias

class CustomActivationFunction(Function):
    @staticmethod
    def forward(ctx, input):
        ctx.save_for_backward(input)
        return input ** 2

    @staticmethod
    def backward(ctx, grad_output):
        input, = ctx.saved_tensors
        grad_input = grad_output * 3 * input ** 2
        return grad_input

class CustomLinear(torch.nn.Module):
    def __init__(self, input_features, output_features, bias=True):
        super(CustomLinear, self).__init__()
        self.input_features = input_features
        self.output_features = output_features
        self.weight = torch.nn.Parameter(torch.Tensor(output_features, input_features))
        if bias:
            self.bias = torch.nn.Parameter(torch.Tensor(output_features))
        else:
            self.register_parameter('bias', None)
        self.reset_parameters()

    def reset_parameters(self):
        torch.nn.init.kaiming_uniform_(self.weight, a=math.sqrt(5))
        if self.bias is not None:
            fan_in, _ = torch.nn.init._calculate_fan_in_and_fan_out(self.weight)
            bound = 1 / math.sqrt(fan_in)
            torch.nn.init.uniform_(self.bias, -bound, bound)

    def forward(self, input):
        linear_output = CustomLinearFunction.apply(input, self.weight, self.bias)
        return CustomActivationFunction.apply(linear_output)

    def validate_gradients():
        input_tensor = torch.randn(2, 3, dtype=torch.double, requires_grad=True)
        weight_tensor = torch.randn(3, 3, dtype=torch.double, requires_grad=True)
        bias_tensor = torch.randn(3, dtype=torch.double, requires_grad=True)

        test_input = (input_tensor, weight_tensor, bias_tensor)
        
        custom_linear_func_test = torch.autograd.gradcheck(CustomLinearFunction.apply, test_input, eps=1e-6, atol=1e-4)
        custom_activation_func_test = torch.autograd.gradcheck(CustomActivationFunction.apply, (input_tensor,), eps=1e-6, atol=1e-4)
        
        return custom_linear_func_test and custom_activation_func_test