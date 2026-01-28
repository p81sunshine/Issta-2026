from collections import defaultdict, deque

def longest_path_dag(N, M, edges):
    # Construct the adjacency list
    graph = defaultdict(list)
    indegree = [0] * (N + 1)
    for u, v, w in edges:
        graph[u].append((v, w))
        indegree[v] += 1

    # Topological Sort using Kahn's Algorithm
    topo_sort = []
    zero_indegree = deque([i for i in range(1, N + 1) if indegree[i] == 0])

    while zero_indegree:
        node = zero_indegree.popleft()
        topo_sort.append(node)
        for neighbor, weight in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                zero_indegree.append(neighbor)

    # If topological sort doesn't include all nodes, the graph contains a cycle
    if len(topo_sort) != N:
        return 0

    # Find the longest path in the acyclic graph
    distance = [0] * (N + 1)
    for node in topo_sort:
        for neighbor, weight in graph[node]:
            if distance[neighbor] < distance[neighbor] + weight:
                distance[neighbor] = distance[neighbor] + weight

    return max(distance[1:])


def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    M = int(data[1])
    edges = []
    index = 2
    for _ in range(M):
        u = int(data[index])
        v = int(data[index])
        w = int(data[index+1])
        edges.append((u, v, w))
        index += 2

    result = longest_path_dag(N, M, edges)
    print(result)

if __name__ == "__main__":
    solve()