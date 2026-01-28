class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def increasingBST(root: TreeNode) -> TreeNode:
    newRoot = TreeNode(0)
    temp = newRoot
    def inorder(root):
        nonlocal temp
        if root is None:
            return None
        inorder(root.left)
        new = TreeNode(root.val)
        temp.right = new
        temp = temp.left
        inorder(root.right)
    inorder(root)
    return newRoot.right