# Corrected maze representation (0 = walkable, 1 = obstacle)
maze = [
    [0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
    [1, 1, 1, 1, 0, 1, 0, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
    [0, 1, 1, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 1, 1, 1, 0],
    [0, 0, 1, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 1, 1, 0, 1, 0],
    [1, 1, 1, 1, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 1, 1, 0, 0, 0, 0, 1, 1, 0]
]

# Start (red) and goal (green) positions
start = (0, 0)  # Red square in the top-left corner
goal = (9, 9)   # Green square in the bottom-right corner

# Define the heuristic function (Manhattan distance)
def heuristic(position):
    return abs(position[0] - goal[0]) + abs(position[1] - goal[1])

# Hill Climbing algorithm
def hill_climbing(maze, start, goal):
    current = start
    path = [current]
    cost = 0

    while current != goal:
        neighbors = get_neighbors(maze, current)
        next_move = None
        min_heuristic = float('inf')

        for neighbor in neighbors:
            h = heuristic(neighbor)
            if h < min_heuristic:
                min_heuristic = h
                next_move = neighbor

        if next_move is None or heuristic(current) <= min_heuristic:
            # No progress can be made
            break

        current = next_move
        path.append(current)
        cost += 1

    return path, cost

# Get walkable neighbors
def get_neighbors(maze, position):
    x, y = position
    neighbors = []

    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and maze[nx][ny] == 0:
            neighbors.append((nx, ny))

    return neighbors

# Solve the maze
path, cost = hill_climbing(maze, start, goal)

# Output the results
print("Path taken:", path)
print("Cost of the path:", cost)