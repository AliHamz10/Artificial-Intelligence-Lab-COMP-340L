import heapq

GOAL_STATE = ((1, 2, 3),
              (4, 5, 6),
              (7, 8, 0))  # 0 represents the blank tile

def manhattan_distance(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            val = state[i][j]
            if val != 0:
                goal_i, goal_j = (val - 1) // 3, (val - 1) % 3
                distance += abs(i - goal_i) + abs(j - goal_j)
    return distance

def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def move(state, direction):
    i, j = find_blank(state)
    new_state = [list(row) for row in state]
    moves = {'up': (i - 1, j), 'down': (i + 1, j), 'left': (i, j - 1), 'right': (i, j + 1)}

    if direction in moves:
        ni, nj = moves[direction]
        if 0 <= ni < 3 and 0 <= nj < 3:
            new_state[i][j], new_state[ni][nj] = new_state[ni][nj], new_state[i][j]
            return tuple(tuple(row) for row in new_state)
    return None

def generate_children(state):
    return [(child, dir) for dir in ['up', 'down', 'left', 'right'] if (child := move(state, dir))]

def beam_search(start_state, beam_width=5, max_depth=50):
    visited = set()
    beam = [(manhattan_distance(start_state), 0, start_state, [])]

    while beam:
        next_beam = []
        for h, depth, state, path in beam:
            if state == GOAL_STATE:
                return path

            if depth >= max_depth:
                continue

            visited.add(state)
            for child, move_dir in generate_children(state):
                if child not in visited:
                    next_beam.append((manhattan_distance(child), depth + 1, child, path + [move_dir]))

        beam = heapq.nsmallest(beam_width, next_beam, key=lambda x: x[0])

    return None

# Solvable initial state
initial_state = ((1, 2, 3),
                 (4, 5, 6),
                 (7, 0, 8))

solution = beam_search(initial_state, beam_width=5)

if solution:
    print(f"Solution found in {len(solution)} moves:")
    print(" -> ".join(solution))
else:
    print("No solution found within limits.")