"""
Find solution to the 8 puzzle problem using iterative depth first search.
"""

from collections import deque

# Define the goal state
goal_state = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

# Define the possible moves
moves = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}


# Function to print the board
def print_board(board):
    for row in board:
        print(' '.join(str(cell) for cell in row))
    print()


# Function to find the blank space (zero position)
def find_zero(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j
    return None


# Function to apply a move to the board
def apply_move(state, move):
    zero_pos = find_zero(state)
    new_pos = (zero_pos[0] + moves[move][0], zero_pos[1] + moves[move][1])

    # Check if the new position is within bounds
    if 0 <= new_pos[0] < 3 and 0 <= new_pos[1] < 3:
        new_state = [row[:] for row in state]  # Create a copy of the current state
        # Swap the zero with the target position
        new_state[zero_pos[0]][zero_pos[1]], new_state[new_pos[0]][new_pos[1]] = new_state[new_pos[0]][new_pos[1]], \
        new_state[zero_pos[0]][zero_pos[1]]
        return new_state
    return None


# Function to perform depth-limited search
def dls(state, depth, visited):
    if state == goal_state:
        return []
    if depth == 0:
        return None

    visited.add(tuple(map(tuple, state)))  # Add the current state to visited

    for move in moves:
        new_state = apply_move(state, move)
        if new_state and tuple(map(tuple, new_state)) not in visited:
            result = dls(new_state, depth - 1, visited)
            if result is not None:
                return [move] + result  # Return the move sequence if found

    visited.remove(tuple(map(tuple, state)))  # Backtrack
    return None


# Function to perform iterative deepening depth-first search
def iddfs(start_state):
    depth = 0
    while True:
        visited = set()
        result = dls(start_state, depth, visited)
        if result is not None:
            return result  # Return the solution if found
        depth += 1  # Increase depth limit


# Main function to execute the algorithm
if __name__ == "__main__":
    start_state = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 0, 8]
    ]

    print("Initial State:")
    print_board(start_state)

    solution = iddfs(start_state)

    if solution:
        print("Solution found:")
        for move in solution:
            print(f"Move: {move}")
            start_state = apply_move(start_state, move)
            print_board(start_state)
    else:
        print("No solution found.")