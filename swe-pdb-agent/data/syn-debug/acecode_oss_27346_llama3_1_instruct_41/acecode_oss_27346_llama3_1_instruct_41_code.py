"""
You are tasked with creating a Python function that processes a list of 3D mesh dimensions and collects information about their bounding boxes.

The function should take in a list of mesh dimensions, where each dimension is represented as a tuple of three floats (length, width, height),
and an optional boolean flag indicating whether the bounding boxes should be oriented or not.

The function should return a list of bounding boxes, where each bounding box is represented as a dictionary containing the following keys:
'min' (a tuple of three floats representing the minimum corner of the bounding box) and 'max' (a tuple of three floats representing the maximum corner of the bounding box).

If the 'oriented' flag is set to True, the bounding box should be computed considering the orientation, otherwise, it should be axis-aligned.

The function signature should be:
`def compute_bounding_boxes(mesh_dimensions: List[Tuple[float, float, float]], oriented: bool = False) -> List[Dict[str, Tuple[float, float, float]]]:`
"""
from typing import List, Tuple, Dict

def compute_bounding_boxes(mesh_dimensions: List[Tuple[float, float, float]], oriented: bool = False) -> List[Dict[str, Tuple[float, float, float]]]:
    """
    Compute the bounding boxes for a list of 3D mesh dimensions.

    Args:
    mesh_dimensions (List[Tuple[float, float, float]]): A list of mesh dimensions, where each dimension is represented as a tuple of three floats (length, width, height).
    oriented (bool, optional): A boolean flag indicating whether the bounding boxes should be oriented or not. Defaults to False.

    Returns:
    List[Dict[str, Tuple[float, float, float]]]: A list of bounding boxes, where each bounding box is represented as a dictionary containing the 'min' and 'max' corners.
    """
    # Initialize an empty list to store the bounding boxes
    bounding_boxes = []

    # Iterate over each mesh dimension
    for dimension in mesh_dimensions:
        # Initialize the minimum and maximum corners for the current bounding box
        min_corner = (0.0, 0.0, 0.0)
        max_corner = (dimension[0], dimension[1], dimension[2])

        # If the 'oriented' flag is set to True, swap the length and width coordinates
        if oriented:
            max_corner = (max_corner[2], max_corner[1], max_corner[0])

        # Create a dictionary representing the current bounding box
        bounding_box = {
            'min': min_corner,
            'max': max_corner
        }

        # Append the bounding box to the list
        bounding_boxes.append(bounding_box)

    # Return the list of bounding boxes
    return bounding_boxes

# Test cases