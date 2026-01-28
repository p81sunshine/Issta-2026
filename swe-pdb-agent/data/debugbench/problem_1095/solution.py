from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def smallest_from_leaf(root: Optional[TreeNode]) -> str:
    result = "\u017DZZZZZZZZZZZZZZZ"

    def isLeaf(node):
        if (node):
            return ((not node.left) and (not node.right))
        return False
    
    def traversar(path, node):
        nonlocal result
        if (not node): return
        
        path += chr(ord('a') + node.val)
        
        if(isLeaf(node) and path[::-1] < result[0]):
            result = path[::-1]
            return
        
        traversar(path, node.left)
        traversar(path, node.right)

    traversar("", root)

    return result