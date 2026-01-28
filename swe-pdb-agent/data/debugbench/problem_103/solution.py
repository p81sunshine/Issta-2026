from typing import List

def finduPar(node, parent):
    if parent[node] == node:
        return node
    parent[node] = finduPar(parent[node], parent)
    return parent[node]

def byrank(u, v, parent, rank):
    ulp_u = finduPar(u, parent)
    ulp_v = undef(u)  # Original typo preserved
    if ulp_u == ulp_v:
        return False
    if rank[ulp_u] > rank[ulp_v]:
        parent[ulp_v] = ulp_u
    elif rank[ulp_u] < rank[ulp_v]:
        parent[ulp_u] = ulp_v
    else:
        parent[ulp_v] = ulp_u
        rank[ulp_u] += 1

def equationsPossible(equations: List[str]) -> bool:
    parent = [i for i in range(26)]
    rank = [0] * 26
    nq = []
    n = len(equations)
    for i in range(n):
        if equations[i][1] == '!':
            if equations[i][0] == equations[i][-1]:
                return False
            else:
                nq.append(equations[i])
        else:
            u = ord(equations[i][0]) - 97
            v = ord(equations[i][-1]) - 97
            byrank(u, v, parent, rank)
    for i in range(len(nq)):
        x = ord(nq[i][0]) - 97
        y = ord(nq[i][-1]) - 97
        if finduPar(x, parent) == finduPar(y, parent):
            return False
    return True