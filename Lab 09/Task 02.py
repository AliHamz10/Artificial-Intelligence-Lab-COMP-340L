import numpy as np

# Define the maze
maze = [
    [1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1],
    [1, 1, 0, 1, 1],
    [0, 1, 0, 1, 0],
    [1, 1, 1, 1, 2]
]

# Define starting point (green) and goal point (red)
start = (0, 0)  # Replace with green's coordinates
goal = (4, 4)   # Replace with red's coordinates

# Hill climbing algorithm with random restarts
def hill_climbing_with_restarts(maze, start, goal, max_restarts=10):
    def heuristic(coord):
        """Calculate Manhattan distance to the goal."""
        return abs(coord[0] - goal[0]) + abs(coord[1] - goal[1])

    # Possible moves (down, up, right, left)
    moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def print_maze(maze, path):
        """Print the maze with the path marked."""
        maze_copy = np.array(maze, dtype=str)
        for r in range(len(maze_copy)):
            for c in range(len(maze_copy[0])):
                if maze_copy[r][c] == '1':
                    maze_copy[r][c] = '.'
                elif maze_copy[r][c] == '2':
                    maze_copy[r][c] = 'G'
                elif maze_copy[r][c] == '0':
                    maze_copy[r][c] = '#'

        for step in path:
            maze_copy[step[0]][step[1]] = 'P'

        for row in maze_copy:
            print(" ".join(row))
        print("\n")

    for restart in range(max_restarts):
        print(f"Restart {restart + 1}/{max_restarts}")
        current = start
        path = [current]
        cost = 0
        visited = set()

        while current != goal:
            visited.add(current)
            neighbors = []
            for move in moves:
                neighbor = (current[0] + move[0], current[1] + move[1])
                # Check if neighbor is within bounds, not an obstacle, and not visited
                if (0 <= neighbor[0] < len(maze) and 0 <= neighbor[1] < len(maze[0])
                        and maze[neighbor[0]][neighbor[1]] != 0 and neighbor not in visited):
                    neighbors.append(neighbor)

            # Sort neighbors by heuristic (ascending)
            neighbors.sort(key=heuristic)

            # Check if there's a better neighbor to move to
            if neighbors and heuristic(neighbors[0]) < heuristic(current):
                current = neighbors[0]
                path.append(current)
                cost += 1
                print(f"Moving to {current} (Heuristic: {heuristic(current)})")
                print_maze(maze, path)
            else:
                print("Stuck in a local minimum, restarting...\n")
                break

        if current == goal:
            print("\nReached the goal!")
            print(f"Path length: {len(path)}")
            return path, cost

    print("Failed to find a solution after maximum restarts.")
    return None, None

# Solve the maze
path, cost = hill_climbing_with_restarts(maze, start, goal)

# Print the results
if path:
    print("Path followed:", path)
    print("Cost of the path:", cost)
else:
    print("No path found.")