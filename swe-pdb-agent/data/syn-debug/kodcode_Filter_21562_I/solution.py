from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if not self.root:
            self.root = TreeNode(val)
        else:
            self._insert_recursive(self.root, val)

    def _insert_recursive(self, node, val):
        if val < node.val:
            if node.left is None:
                node.left = TreeNode(val)
            else:
                self._insert_recursive(node.left, val)
        else:
            if node.right is None:
                node.right = TreeNode(val)
            else:
                self._insert_recursive(node.right, val)

    def dfs_combinations(self):
        if not self.root:
            return []
        
        result = []
        def dfs(node, path):
            if node:
                path.append(node.val)
                result.append(path)
                dfs(node.left, path)
                dfs(node.right, path)
                path.pop()
        
        dfs(self.root, [])
        return result

    def bfs_combinations(self):
        if not self.root:
            return []
        
        result = []
        queue = deque([(self.root, [])])
        
        while queue:
            node, path = queue.popleft()
            path.append(node.val)
            result.append(path)
            if node.left:
                queue.append((node.left, path))
            if node.right:
                queue.append((node.right, path))
        
        return result