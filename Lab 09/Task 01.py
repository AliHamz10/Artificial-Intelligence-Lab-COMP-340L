# Hill Climbing Algorithm for Maze Problem

# Define the maze as a grid
maze = [
    ['A', 'B', 'C', 'D', 'E', 'F'],  # Row 0
    ['F', 'G', '-', '-', '-', '-'],  # Row 1
    ['H', 'I', 'J', 'K', 'L', '-'],  # Row 2
    ['M', 'N', 'O', 'P', 'Q', '-'],  # Row 3
    ['R', 'S', 'T', 'U', 'V', 'Y']   # Row 4
]

# Define blocked cells (blue cells)
blocked_cells = {
    (0, 1), (0, 2), (0, 4),  # B, C, E in Row 0
    (1, 1),                  # G in Row 1
    (2, 0),                  # H in Row 2
    (3, 1),                  # N in Row 3
    (4, 2)                   # W in Row 4
}

# Define start and goal coordinates
start = (0, 0)  # Starting at 'A'
goal = (4, 5)   # Goal is 'Y'

# Manhattan distance as the heuristic
def manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

# Get valid neighbors of the current position
def get_neighbors(position):
    x, y = position
    neighbors = [
        (x - 1, y),  # Up
        (x + 1, y),  # Down
        (x, y - 1),  # Left
        (x, y + 1)   # Right
    ]
    # Filter out-of-bounds and blocked cells
    valid_neighbors = [
        (nx, ny) for nx, ny in neighbors
        if 0 <= nx < 5 and 0 <= ny < 6 and (nx, ny) not in blocked_cells
    ]
    return valid_neighbors

# Hill Climbing algorithm
def hill_climbing(start, goal):
    current_position = start
    path = [current_position]

    while current_position != goal:
        neighbors = get_neighbors(current_position)

        if not neighbors:  # No valid neighbors, stuck in local maximum
            print("Stuck at local maximum!")
            break

        # Sort neighbors by heuristic (Manhattan distance to the goal)
        neighbors.sort(key=lambda pos: manhattan_distance(pos[0], pos[1], goal[0], goal[1]))

        # Choose the best neighbor (lowest heuristic value)
        best_neighbor = neighbors[0]

        # If the best neighbor is worse than or equal to the current position, stop
        if manhattan_distance(best_neighbor[0], best_neighbor[1], goal[0], goal[1]) >= \
                manhattan_distance(current_position[0], current_position[1], goal[0], goal[1]):
            print("Stuck at local maximum!")
            break

        # Move to the best neighbor
        current_position = best_neighbor
        path.append(current_position)

    return path

# Solve the maze
path = hill_climbing(start, goal)

# Print the result
print("Path taken:")
for step in path:
    print(step)