# Problem: Implement a function `dyadic_permutation_search(num_list: List[int], search_perm: Tuple[int, int]) -> bool`
#          that takes a list of unique integers `num_list` and a tuple `search_perm`.
#          The function should return `True` if the dyadic permutation (an ordered pair of two distinct integers from the list)
#          represented by `search_perm` exists in the binary search tree constructed from all possible dyadic permutations of the integers in `num_list`.
#          Otherwise, it should return `False`.

from typing import List, Tuple

class Node:
    """Represents a node in the binary search tree."""
    
    def __init__(self, key: Tuple[int, int]):
        """
        Initializes a node with a key and two children nodes.
        
        Args:
        key (Tuple[int, int]): A tuple representing a dyadic permutation.
        """
        self.key = key
        self.left = None
        self.right = None


def insert(root: Node, key: Tuple[int, int]) -> Node:
    """
    Inserts a key into the binary search tree.
    
    Args:
    root (Node): The root of the binary search tree.
    key (Tuple[int, int]): A tuple representing a dyadic permutation.
    
    Returns:
    Node: The root of the updated binary search tree.
    """
    if root is None:
        return Node(key)
    
    if key[0] < root.key[0]:
        root.left = insert(root.left, key)
    elif key[0] > root.key[0]:
        root.right = insert(root.right, key)
    elif key[0] == root.key[0]:
        if key[1] < root.key[1]:
            root.left = insert(root.left, key)
        elif key[1] > root.key[1]:
            root.right = insert(root.right, key)
        else:
            return root
    
    return root


def inorder(root: Node) -> List[Tuple[int, int]]:
    """
    Performs an inorder traversal of the binary search tree and returns a list of keys.
    
    Args:
    root (Node): The root of the binary search tree.
    
    Returns:
    List[Tuple[int, int]]: A list of keys in the binary search tree.
    """
    res = []
    if root:
        res = inorder(root.left)
        res.append(root.key)
        res = res + inorder(root.right)
    return res


def dyadic_permutation_search(num_list: List[int], search_perm: Tuple[int, int]) -> bool:
    """
    Searches for a dyadic permutation in the binary search tree constructed from all possible dyadic permutations of the integers in `num_list`.
    
    Args:
    num_list (List[int]): A list of unique integers.
    search_perm (Tuple[int, int]): A tuple representing a dyadic permutation.
    
    Returns:
    bool: `True` if the dyadic permutation exists in the binary search tree, `False` otherwise.
    """
    # Generate all possible dyadic permutations
    perms = [(min(x, y), max(x, y)) for x in num_list for y in num_list if x != y]
    
    # Create the binary search tree
    root = None
    for perm in perms:
        root = insert(root, perm)
    
    # Perform an inorder traversal and check if the search permutation exists
    return search_perm in inorder(root)


# Test cases