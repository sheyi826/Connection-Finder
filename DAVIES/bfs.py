from collections import deque

def bfs_find_path(graph, start, goal):
    # 1. Handle cases where names aren't in the data
    if start not in graph or goal not in graph:
        return None

    # 2. The Queue stores the entire path so far
    queue = deque([[start]])
    # 3. The Visited set prevents infinite loops
    visited = {start}

    while queue:
        # Pop the oldest path from the left (FIFO)
        current_path = queue.popleft()
        # The 'current_node' is the last person in that path
        current_node = current_path[-1]

        # 4. Check if we reached the goal
        if current_node == goal:
            return current_path

        # 5. Explore neighbors (friends)
        for neighbor in graph.get(current_node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                # Create a NEW path list to add to the queue
                new_path = list(current_path)
                new_path.append(neighbor)
                queue.append(new_path)

    return None # No connection found