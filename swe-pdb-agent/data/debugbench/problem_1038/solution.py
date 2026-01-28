from queue import Queue
from typing import List

def frogPosition(n: int, edges: List[List[int]], t: int, target: int) -> float:
    if edges == []:
        if target == 1: return 1
        return 0

    d = {}
    for i in edges:
        d[i[0]] = d.get(i[0] , []) + [i[1]]
        d[i[1]] = d.get(i[1] , []) + [i[0]]
    
    visit = [0]*(n+1)

    q = Queue()     
    q.put([1 , 1])

    for dur in range(t+1):
        
        l = q.qsize()
        for i in range(l):
            temp = q.get()

            count = 0
            for ele in d[temp[0]]:
                if visit[ele] == 0: count += 1

            if temp[0] == target and count == 0:     
                return temp[1]
                
            if visit[temp[0]] != 0:    
                continue
                
            visit[temp[0]] = 1

            for ele in d[temp[0]]:
                if visit[ele] == 0: q.put([ele , temp[1]*(1/count)])
                
        
    l = q.qsize()
    for i in range(l):
        temp = q.get()
        if temp[0] == target:
            return temp[1]

    return 0