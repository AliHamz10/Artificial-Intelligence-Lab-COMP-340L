import heapq

def beam_search(grid, start, goal, beam_width):
    rows, cols = len(grid), len(grid[0])

    # Directions: up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # Beam: (cumulative_cost, current_path)
    beam = [(grid[start[0]][start[1]], [start])]

    while beam:
        next_beam = []

        for cost, path in beam:
            x, y = path[-1]

            if (x, y) == goal:
                return path, cost

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in path:
                    cell_cost = grid[nx][ny]
                    if cell_cost is not None:  # Handle obstacle
                        new_cost = cost + cell_cost
                        new_path = path + [(nx, ny)]
                        next_beam.append((new_cost, new_path))

        # Keep only the top `beam_width` paths with least cost
        beam = heapq.nsmallest(beam_width, next_beam, key=lambda x: x[0])

    return None, float('inf')  # If no path is found

# Example Grid
# 0s are obstacles (set to None), other numbers are costs
grid = [
    [1, 4, 1, 2],
    [1, None, 3, 1],
    [2, 1, None, 2],
    [3, 2, 1, 1]
]

start = (0, 0)
goal = (3, 3)
beam_width = 2

path, total_cost = beam_search(grid, start, goal, beam_width)

print("Shortest Path:", path)
print("Total Cost:", total_cost)