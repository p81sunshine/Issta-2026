from solution import *

def parse_input(input_str):
    start = input_str.find("[")
    end = input_str.rfind("]")
    if start == -1 or end == -1:
        raise ValueError("Invalid input format")
    elements = input_str[start+1:end].split(",")
    values = []
    for elem in elements:
        elem = elem.strip()
        if elem.lower() == "null":
            values.append(None)
        else:
            values.append(int(elem))
    return values

def build_tree(values):
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    while queue and i < len(values):
        current = queue.pop(0)
        if values[i] is not None:
            current.left = TreeNode(values[i])
            queue.append(current.left)
        i += 1
        if i < len(values) and values[i] is not None:
            current.right = TreeNode(values[i])
            queue.append(current.right)
        i += 1
    return root

def test_example_1():
    input_str = "Input: root = [2,1,3]\nOutput: 1"
    expected = 1
    values = parse_input(input_str)
    root = build_tree(values)
    assert findBottomLeftValue(root) == expected, "Example 1 failed"

def test_example_2():
    input_str = "Input: root = [1,2,3,4,null,5,6,null,null,7]\nOutput: 7"
    expected = 7
    values = parse_input(input_str)
    root = build_tree(values)
    assert findBottomLeftValue(root) == expected, "Example 2 failed"

def test_single_node():
    input_str = "Input: root = [5]\nOutput: 5"
    expected = 5
    values = parse_input(input_str)
    root = build_tree(values)
    assert findBottomLeftValue(root) == expected, "Single node test failed"

def test_left_skewed_tree():
    input_str = "Input: root = [5,4,null,3,null,null,null]\nOutput: 3"
    expected = 3
    values = parse_input(input_str)
    root = build_tree(values)
    assert findBottomLeftValue(root) == expected, "Left skewed tree test failed"

def test_last_level_multiple_nodes():
    input_str = "Input: root = [5,3,7,2,4,null,null]\nOutput: 2"
    expected = 2
    values = parse_input(input_str)
    root = build_tree(values)
    assert findBottomLeftValue(root) == expected, "Last level multiple nodes test failed"