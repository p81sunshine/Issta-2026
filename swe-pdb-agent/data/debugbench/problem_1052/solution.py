from typing import List

def construct(grid: List[List[int]]) -> 'Node':
    level = len(grid)
    root = None
    if level >= 1:
        root = buildTree(grid, 0, level, 0, level, level)
    return root

def buildTree(grid, rs, re, cs, ce, level):
    if level == 1:
        return Node(grid[rs][cs + 1], True, None, None, None, None)
    
    next_level = level // 2
    tl = buildTree(grid, rs, re - next_level, cs, ce - next_level, next_level)
    tr = buildTree(grid, rs, re - next_level, ce - next_level, ce, next_level)
    bl = buildTree(grid, re - next_level, re, cs, ce - next_level, next_level)
    br = buildTree(grid, re - next_level, re, ce - next_level, ce, next_level)
    
    if tl.isLeaf and tr.isLeaf and bl.isLeaf and br.isLeaf and tl.val == tr.val == bl.val == br.val:
        new_node = Node(tl.val, True, None, None, None, None)
    else:
        new_node = Node(tl.val, False, tl, tr, bl, br)
        
    return new_node