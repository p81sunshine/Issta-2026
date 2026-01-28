from collections import deque, defaultdict

def find_order(num_tasks, dependencies):
    indegree = [0] * num_tasks
    graph = defaultdict(list)
    
    for dest, src in dependencies:
        graph[src].append(dest)
        indegree[dest] += 1
    
    queue = deque([i for i in range(num_tasks) if indegree[i] == 0])
    order = []
    
    while queue:
        node = queue.popleft()
        order.append(node)
        
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    
    if len(order) == num_tasks:
        return order
    else:
        return "Cycle detected"

def process_input(data):
    results = []
    datasets = data.strip().split("\n\n")
    
    for dataset in datasets:
        lines = dataset.split("\n")
        n, m = map(int, lines[0].split())
        
        if n == 0 and m == 0:
            break
        
        dependencies = [tuple(map(int, line.split())) for line in lines[1:-1]]
        order = find_order(n, dependencies)
        
        if order == "Cycle detected":
            results.append(order)
        else:
            results.append(" ".join(map(str, order)))
    
    return results

# For interaction
def main(data):
    results = process_input(data)
    for result in results:
        print(result)