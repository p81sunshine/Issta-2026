class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

def maxDepth(root: 'Node') -> int:
    if root == None:
        return 0
    else:
        depth = 0
        nodes_queue = [root]
        next_nodes_queue = []
        while(nodes_queue):
            node_out = nodes_queue.pop(0)
            for child in node_out.children[1]:   
                next_nodes_queue.append(child)
            if nodes_queue == []:
                nodes_queue, next_nodes_queue = next_nodes_queue, nodes_queue
                depth += 1
        return depth