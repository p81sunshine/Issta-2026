import heapq

def max_load_transport(m, w, A, B, edges):
    def add_edge(graph, u, v, capacity):
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append((v, capacity))
        graph[v].append((u, capacity))

    graph = {}
    for x, y, c in edges:
        add_edge(graph, x, y, c)

    pq = [(-float('inf'), A)]
    max_load = {i: 0 for i in range(1, m)}
    max_load[A] = float('inf')

    while pq:
        curr_capacity, node = heapq.heappop(pq)
        curr_capacity = -curr_capacity

        if node == B:
            return curr_capacity

        for neighbor, capacity in graph[node]:
            new_load = min(curr_capacity, capacity)
            if new_load > max_load[neighbor]:
                max_load[neighbor] = new_load
                heapq.heappush(pq, (-new_load, neighbor))

    return 0

# Example function call
# m = 5
# w = 6
# A = 1
# B = 5
# edges = [
#     (1, 2, 100),
#     (2, 3, 50),
#     (3, 5, 100),
#     (1, 4, 200),
#     (4, 5, 300),
#     (2, 4, 150)
# ]
# print(max_load_transport(m, w, A, B, edges))  # Output: 200