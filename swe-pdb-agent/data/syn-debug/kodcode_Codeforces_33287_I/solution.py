from collections import deque

def min_swaps_to_sort_sequence(n, k, arr):
    # Helper function to perform BFS to find the smallest distance
    def bfs(start, graph, visited):
        queue = deque([start])
        visited[start] = True
        component = []
        while queue:
            node = queue.popleft()
            component.append(node)
            for neighbour in graph[node]:
                if not visited[neighbour]:
                    visited[neighbour] = True
                    queue.append(neighbour)
        return component

    # Create nodes based on their positions in the sorted array
    sorted_arr = sorted(arr)
    lookup = {value: i for i, value in enumerate(arr)}
    
    # Create the graph for allowed swaps
    graph = {i: [] for i in range(n)}
    for i in range(n):
        for j in range(i + 1, n):
            if abs(arr[i] - arr[j]) <= k:
                graph[i].append(j)
                graph[j].append(i)

    visited = [False] * n
    swaps = 0

    # Find all connected components in the graph
    for i in range(n):
        if not visited[i]:
            component = bfs(i, graph, visited)
            component_values = [arr[x] for x in component]
            sorted_component_values = sorted(component_values)
            for idx, val in zip(component, sorted_component_values):
                if arr[idx] != val:
                    swaps += 1

    for i in range(n):
        if arr[i] != sorted_arr[i]:
            return -1

    return swaps // 2  # Each swap is counted twice, so divide by 2.