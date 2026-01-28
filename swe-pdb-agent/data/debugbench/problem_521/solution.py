from collections import deque, defaultdict

def amountOfTime(root, start):
    graph = defaultdict(list)
    
    stack = [(root, None)]
    while stack: 
        n, p = stack.pop()
        if p: 
            graph[p.val].append(n.val)
            graph[n.val].append(p.val)
        if n.left: stack.append((n.left, n))
        if n.right: stack.append((n.right, n))
    
    ans = 0  
    seen = {start}
    queue = deque([start])
    while queue: 
        for _ in range(len(queue)): 
            u = queue.pop()
            for v in graph[u]: 
                if v not in seen: 
                    seen.add(v)
                    queue.append(v)
        ans += 1
    return ans