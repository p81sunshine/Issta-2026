from typing import List, Tuple

def degrees_of_separation(user_id1: int, user_id2: int, friendships: List[Tuple[int, int]]) -> int:
    """
    This function calculates the degree of separation between two users in a social network.

    Args:
    user_id1 (int): The ID of the first user.
    user_id2 (int): The ID of the second user.
    friendships (List[Tuple[int, int]]): A list of tuples representing friendships between users.

    Returns:
    int: The degree of separation between the two users. If there is no connection, returns -1.
    """
    
    # Create an adjacency list to represent the graph
    graph = {}
    for user1, user2 in friendships:
        if user1 not in graph:
            graph[user1] = []
        if user2 not in graph:
            graph[user2] = []
        graph[user1].append(user2)
        graph[user2].append(user1)

    # Check if either user is not in the graph
    if user_id1 not in graph or user_id2 not in graph:
        return -1

    # If the users are the same, return 0
    if user_id1 == user_id2:
        return 0

    # Perform BFS to find the degree of separation
    queue = [(user_id1, 1)]  # Initialize queue with the starting user and a separation of 1
    visited = set()  # Keep track of visited users to avoid infinite loops
    while queue:
        current_user, separation = queue.pop(0)
        if current_user == user_id2:
            return separation
        visited.add(current_user)
        for friend in graph.get(current_user, []):
            if friend not in visited:
                queue.append((friend, separation + 1))

    # If there is no connection between the users, return -1
    return -1

# Test cases