from typing import List, Tuple, Dict, Optional
from collections import defaultdict, deque

def solve_2_sat(formula: List[Tuple[Tuple[str, bool], Tuple[str, bool]]]) -> Optional[Dict[str, bool]]:
    # Helper function to get variable and its negation index
    def get_index(var: str, is_negated: bool) -> int:
        return 2 * variable_index[var] + (1 if is_negated else 0)
    
    # Kosaraju's algorithm to find strongly connected components
    def kosaraju_scc(graph: List[List[int]], n: int):
        # First pass to fill the stack
        def dfs_1(v: int):
            visited[v] = True
            for u in graph[v]:
                if not visited[u]:
                    dfs_1(u)
            stack.append(v)
        
        # Second pass to get SCCs
        def dfs_2(v: int, label: int):
            scc[v] = label
            for u in rev_graph[v]:
                if scc[u] is None:
                    dfs_2(u, label)
        
        visited = [False] * n
        stack = []
        for i in range(n):
            if not visited[i]:
                dfs_1(i)
        
        label_count = 0
        while stack:
            node = stack.pop()
            if scc[node] is None:
                dfs_2(node, label_count)
                label_count += 1
        
        return label_count

    variable_index = {}
    index = 0
    for clause in formula:
        for var, _ in clause:
            if var not in variable_index:
                variable_index[var] = index
                index += 1

    variable_count = len(variable_index)
    graph = [[] for _ in range(2 * variable_count)]
    rev_graph = [[] for _ in range(2 * variable_count)]
    
    for (x, x_neg), (y, y_neg) in formula:
        xi = get_index(x, not x_neg)
        yi = get_index(y, y_neg)
        graph[xi].append(yi)
        rev_graph[yi].append(xi)
        
        yi = get_index(y, not y_neg)
        xi = get_index(x, x_neg)
        graph[yi].append(xi)
        rev_graph[xi].append(yi)
    
    scc = [None] * (2 * variable_count)
    kosaraju_scc(graph, 2 * variable_count)
    
    assignment = {}
    for var, idx in variable_index.items():
        if scc[2 * idx] == scc[2 * idx + 1]:
            return None
        assignment[var] = scc[2 * idx + 1] > scc[2 * idx]
    
    return assignment
