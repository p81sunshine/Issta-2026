from solution import *

import math

from solution import *

import math

from solution import *

import math

import torch
from torch import nn
from typing import Tuple, Dict, Any
from solution import export_ir_metadata

def test_export_ir_metadata():
    class SimpleModel(nn.Module):
        def forward(self, x, y):
            return x + y

    model = SimpleModel()
    example_args = (torch.randn(3, 3), torch.randn(3, 3))
    
    result = export_ir_metadata(model, example_args)
    
    # Check if the result contains expected keys
    assert "graph_structure" in result
    assert "nodes_metadata" in result
    
    # Check if nodes_metadata contains metadata of at least one node
    assert len(result["nodes_metadata"]) > 0
    
    # Check the structure of the metadata of the first node
    first_node_metadata = result["nodes_metadata"][0]
    assert "name" in first_node_metadata
    assert "op_name" in first_node_metadata
    assert "stack_trace" in first_node_metadata
    assert "val" in first_node_metadata
    assert "nn_module_stack" in first_node_metadata
    assert "source_fn_stack" in first_node_metadata

def test_empty_model():
    class EmptyModel(nn.Module):
        def forward(self, x):
            return x

    model = EmptyModel()
    example_args = (torch.randn(1, 1),)
    
    result = export_ir_metadata(model, example_args)
    
    # Check if the result contains expected keys
    assert "graph_structure" in result
    assert "nodes_metadata" in result
    
    # Check if nodes_metadata contains metadata
    assert len(result["nodes_metadata"]) == 0  # Expecting no call_function nodes

def test_complex_model():
    class ComplexModel(nn.Module):
        def forward(self, x, y, z):
            return (x + y) * z

    model = ComplexModel()
    example_args = (torch.randn(2, 2), torch.randn(2, 2), torch.randn(2, 2))
    
    result = export_ir_metadata(model, example_args)
    
    # Check if the result contains expected keys
    assert "graph_structure" in result
    assert "nodes_metadata" in result
    
    # Check if nodes_metadata contains metadata of at least one node
    assert len(result["nodes_metadata"]) > 0

    # Check the structure of the metadata of the first node
    first_node_metadata = result["nodes_metadata"][0]
    assert "name" in first_node_metadata
    assert "op_name" in first_node_metadata
    assert "stack_trace" in first_node_metadata
    assert "val" in first_node_metadata
    assert "nn_module_stack" in first_node_metadata
    assert "source_fn_stack" in first_node_metadata