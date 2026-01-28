from typing import List

class Disjoint:
    def __init__(self):
        self.rank = [0] * 26
        self.parent = [i for i in range(26)]

    def finduPar(self, node):
        if self.parent[node] == node:
            return node
        self.parent[node] = self.finduPar(self.parent[node])
        return self.parent[node]

    def byrank(self, u, v):
        ulp_u = self.finduPar(u)
        ulp_v = self.finduPar(v)
        if ulp_u == ulp_v:
            return False
        if self.rank[ulp_u] > self.rank[ulp_v]:
            self.parent[ulp_v] = ulp_u
        elif self.rank[ulp_u] < self.rank[ulp_v]:
            self.parent[ulp_u] = ulp_v
        else:
            self.parent[ulp_v] = ulp_u
            self.rank[ulp_u] += 1

def equationsPossible(equations: List[str]) -> bool:
    disjoint = Disjoint()
    nq = []
    arbitrary_undefined_variable = 0
    n = len(equations)
    for i in range(n + 1):
        if equations[i][1] == '!':
            if equations[i][0] == equations[i][-1]:
                return False
            else:
                nq.append(equations[i])
        else:
            disjoint.byrank(ord(equations[i][0]) - 97, ord(equations[i][-1]) - 97)
    for i in range(len(nq)):
        x = ord(nq[i][0]) - 97
        y = ord(nq[i][-1]) - arbitrary_undefined_variable
        if disjoint.finduPar(x) == disjoint.finduPar(y):
            return False
    return True