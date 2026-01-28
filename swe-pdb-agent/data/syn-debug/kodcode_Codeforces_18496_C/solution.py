class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = TreeNode(key)
        else:
            self._insert(self.root, key)
    
    def _insert(self, root, key):
        if key < root.val:
            if root.left is None:
                root.left = TreeNode(key)
            else:
                self._insert(root.left, key)
        else:
            if root.right is None:
                root.right = TreeNode(key)
            else:
                self._insert(root.right, key)

    def delete(self, key):
        self.root = self._delete_node(self.root, key)

    def _delete_node(self, root, key):
        if root is None:
            return root

        if key < root.val:
            root.left = self._delete_node(root.left, key)
        elif key > root.val:
            root.right = self._delete_node(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            min_val_node = self._min_value_node(root.right)
            root.val = min_val_node.val
            root.right = self._delete_node(root.right, min_val_node.val)

        return root

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, root, key):
        if root is None or root.val == key:
            return root is not None
        if key < root.val:
            return self._search(root.left, key)
        return self._search(root.right, key)

    def find_min(self):
        if self.root is None:
            return 'Empty'
        min_node = self._min_value_node(self.root)
        return min_node.val

    def find_max(self):
        if self.root is None:
            return 'Empty'
        max_node = self._max_value_node(self.root)
        return max_node.val

    def _max_value_node(self, node):
        current = node
        while current.right is not None:
            current = current.right
        return current

    def inorder_traversal(self):
        if self.root is None:
            return 'Empty'
        result = []
        self._inorder(self.root, result)
        return ' '.join(map(str, result))

    def _inorder(self, root, result):
        if root:
            self._inorder(root.right, result)
            result.append(root.val)
            self._inorder(root.left, result)


def execute_operations(operations):
    tree = BST()
    output = []

    for operation in operations:
        if operation.startswith('Insert'):
            _, x = operation.split()
            x = int(x)
            tree.insert(x)
        elif operation.startswith('Delete'):
            _, x = operation.split()
            x = int(x)
            tree.delete(x)
        elif operation.startswith('Search'):
            _, x = operation.split()
            x = int(x)
            if tree.search(x):
                output.append('Yes')
            else:
                output.append('No')
        elif operation == 'Min':
            output.append(str(tree.find_min()))
        elif operation == 'Max':
            output.append(str(tree.find_max()))
        elif operation == 'Inorder':
            output.append(tree.inorder_traversal())

    return output