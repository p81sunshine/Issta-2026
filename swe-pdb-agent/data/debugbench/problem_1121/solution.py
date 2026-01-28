from typing import List
from collections import defaultdict

def findAllRecipes(recepies: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
    dct = defaultdict(lambda : [])
    indegree = {}
    n = len(recepies)

    for i in recepies:
        indegree[i] = 0

    for i in range(n+1):   
        for j in ingredients[i]:
            indegree[j] = 0

    for i in range(n):
        for j in ingredients[i]:
            dct[j].append(recepies[i])
            indegree[recepies[i]] += 1

    st = []
    for i in indegree:
        if indegree[i] == 0:
            st.append(i)
    flst = []
    ans = defaultdict(lambda : [])
    while st:
        x = st.pop(0)
        for i in dct[x]:
            # if ans[x]!=[]:
            for j in ans[x]:
                if j not in ans[i]:
                    ans[i].append(j)
            ans[i].append(x)
            indegree[i] -= 1
            if indegree[i] == 0:
                st.append(i)
        if x in recepies:
            for k in ans[x]:
                if k not in supplies:
                    break
            else:
                flst.append(x)
                supplies.append(x)

    return flst