import heapq

def hill_climbing(start, goal, obstacles, rows, cols):
    """
    Hill Climbing algorithm to find a path in the maze.
    """
    def heuristic(node):
        # Manhattan distance
        return abs(node[0] - goal[0]) + abs(node[1] - goal[1])

    def get_neighbors(node):
        # Possible moves: up, down, left, right
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        neighbors = []
        for move in moves:
            new_node = (node[0] + move[0], node[1] + move[1])
            if 0 <= new_node[0] < rows and 0 <= new_node[1] < cols and new_node not in obstacles:
                neighbors.append(new_node)
        return neighbors

    path = [start]
    current = start
    visited = set()

    print(f"Starting Hill Climbing from {start} to {goal}...\n")

    while current != goal:
        visited.add(current)
        neighbors = get_neighbors(current)

        if not neighbors:
            print("No path found! Stuck at local maxima.")
            return path

        # Use a priority queue to select the best neighbor
        priority_queue = []
        for neighbor in neighbors:
            if neighbor not in visited:
                heapq.heappush(priority_queue, (heuristic(neighbor), neighbor))

        if not priority_queue:
            print("No path found! Stuck at local maxima.")
            return path

        # Get the neighbor with the best heuristic value
        _, next_node = heapq.heappop(priority_queue)

        if heuristic(next_node) >= heuristic(current):
            print("No path found! Stuck at local maxima.")
            return path

        print(f"Moving from {current} to {next_node} (Heuristic: {heuristic(next_node)})")
        path.append(next_node)
        current = next_node

    print("\nReached the goal!")
    print(f"Path length: {len(path)}")
    return path


# Maze dimensions
rows, cols = 6, 6

# Obstacles (blue cells)
obstacles = {(0, 2), (0, 3), (0, 4), (1, 2), (1, 4), (2, 0), (2, 4),
             (3, 0), (3, 4), (4, 0), (4, 1), (4, 2), (4, 4)}

# Start and goal positions
start = (0, 0)  # A
goal = (5, 4)   # Y

# Run the Hill Climbing algorithm
path = hill_climbing(start, goal, obstacles, rows, cols)

# Output the path
print("\nPath taken:")
for step in path:
    print(step)