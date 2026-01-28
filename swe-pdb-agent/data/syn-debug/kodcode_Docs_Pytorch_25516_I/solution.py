import torch
from torch import nn
from torch.fx import GraphModule, symbolic_trace
from typing import Tuple, Dict, Any

def export_ir_metadata(model: nn.Module, example_args: Tuple[torch.Tensor, ...]) -> Dict[str, Any]:
    """
    Generates the export IR graph and extracts metadata from the graph nodes.
    """
    # Trace the model to create an FX Graph
    traced = symbolic_trace(model, example_inputs=example_args)

    # Generate a string representation of the graph
    graph_structure = str(traced.graph)

    # Extract nodes metadata
    nodes_metadata = []
    for node in traced.graph.nodes:
        if node.op == "call_function":
            nodes_metadata.append({
                "name": node.name,
                "op_name": node.op,
                "stack_trace": str(node.stack_trace),
                "val": str(node.target),
                "nn_module_stack": str(node.meta.get('nn_module_stack', {})),
                "source_fn_stack": str(node.meta.get('source_fn_stack', {}))
            })

    return {
        "graph_structure": graph_structure,
        "nodes_metadata": nodes_metadata
    }

if __name__ == "__main__":
    class SimpleModel(nn.Module):
        def forward(self, x, y):
            return x + y

    model = SimpleModel()
    example_args = (torch.randn(3, 3), torch.randn(3, 3))
    result = export_ir_metadata(model, example_args)
    print(result)