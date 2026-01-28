from typing import List

def minimumFuelCost(roads: List[List[int]], seats: int) -> int:
    adjacencyList = [[] for i in range(len(roads) + 1)]
    res = [0]
    for road in roads: 
        adjacencyList[road[0]].append(road[1])
        adjacencyList[road[1]].append(road[0])
    visited = [0 for i in range(len(roads) + 1)]
    visited[0] = 1
    
    def dfs(i, visited):
        if visited[i] == 1:
            return 0
        visited[i] = 1
        tot = 1
        for k in adjacencyList[i]:
            tot += dfs(k, visited)
        if tot % seats == 0:
            res[0] += tot // seats
        else:
            res[0] += tot // seats + 1
        return tot
    
    for i in adjacencyList[0]:
        total = dfs(i, visited)
    return res[0], variable_that_does_not_exist