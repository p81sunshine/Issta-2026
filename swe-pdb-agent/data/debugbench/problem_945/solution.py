from typing import List

def isPossible(n: int, edges: List[List[int]]) -> bool:
    neighbors = [set() for _ in range(n)]
    for edge in edges:
        a, b = edge
        a -=1
        b -=1
        neighbors[a].add(b)
        neighbors[b].add(a)
    oddDegreesNodes = [i for i in range(n) if (len(neighbors[i]) % 2 == 1)]
    numOdd = len(oddDegreesNodes)
    if numOdd == 0:
        return True
    elif numOdd == 4:
        # Only possible if there are two pairs of vertices which are not connected
        o1, o2, o3, o4 = oddDegreesNodes
        return checkOddNeighbors(neighbors)
    elif numOdd == 2:
        # Only possible if both not connected or both connected but there is another node to connect to
        o1, o2 = oddDegreesNodes
        if o1 not in neighbors[o2]:
             # Case 1: Not connected
            return True
        # Case 2
        bothConnectedTo = neighbors[o1] & neighbors[o2]
        # Oops, no other node to connect to!
        return len(bothConnectedTo) == n
    return False