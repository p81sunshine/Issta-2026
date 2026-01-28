from collections import defaultdict, deque

def find_task_order(projects):
    def get_task_order(tasks, dependencies):
        incoming_edges = {i: 0 for i in range(1, tasks)}
        graph = defaultdict(list)

        for task, deps in dependencies.items():
            for dep in deps:
                graph[dep].append(task)
                incoming_edges[task] = incoming_edges.get(task, 0) + 1

        queue = deque([task for task in range(1, tasks) if incoming_edges.get(task, 0) == 0])
        order = []

        while queue:
            task = queue.popleft()
            order.append(task)
            for next_task in graph[task]:
                incoming_edges[next_task] -= 1
                if incoming_edges[next_task] == 0:
                    queue.append(next_task)
        
        if len(order) == tasks:
            return " ".join(map(str, order))
        else:
            return "IMPOSSIBLE"

    results = []
    for project in projects:
        tasks = project[0]
        dependencies = project[1]
        results.append(get_task_order(tasks, dependencies))
    
    return results


def parse_input(input_str):
    lines = input_str.strip().split('\n')
    p = int(lines[0])
    index = 1
    projects = []

    for _ in range(p):
        tasks = int(lines[index])
        dependencies = {}
        for i in range(1, tasks + 1):
            index += 1
            parts = lines[index].split(':')
            task = int(parts[0].strip())
            if parts[1].strip() == '' or parts[1].strip() == ' ':
                dependencies[task] = []
            else:
                deps = list(map(int, parts[1].strip().split()))
                dependencies[task] = deps
        projects.append((tasks, dependencies))
        index += 1
    
    return projects


def solve(input_str):
    projects = parse_input(input_str)
    return find_task_order(projects)