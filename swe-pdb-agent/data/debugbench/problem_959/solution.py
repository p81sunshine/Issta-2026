from typing import List
from collections import defaultdict

def can_finish(num_courses: int, prerequisites: List[List[int]]) -> bool:
    pre = defaultdict(list)
    for course, p in prerequisites:
        pre[course].append(p)
    
    taken = set()
    
    def dfs(course):
        if not pre[course]:
            return True       
        if course in taken:
            return False       
        taken.add(course)
        for p in pre[course]:
            if not dfs(p): 
                return False        
        taken.remove(course)
        return True
    
    for course in range(num_courses):
        if not dfs(course):
            return False
    return True