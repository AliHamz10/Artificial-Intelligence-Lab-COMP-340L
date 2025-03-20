from typing import Tuple
import numpy as np

# Gridworld Parameters
ROWS, COLS = 4, 4
ACTIONS = ('UP', 'DOWN', 'LEFT', 'RIGHT')
START, GOAL = (0, 0), (3, 3)
REWARD_GOAL, REWARD_OTHER = 1.0, 0.0
GAMMA, THRESHOLD = 0.9, 1e-4
ACTION_PROB = 1 / len(ACTIONS)  # Uniform action probability

def get_next_state(state: Tuple[int, int], action: str) -> Tuple[int, int]:
    """Returns the next state given a current state and an action."""
    row, col = state
    transitions = {
        'UP': (max(row - 1, 0), col),
        'DOWN': (min(row + 1, ROWS - 1), col),
        'LEFT': (row, max(col - 1, 0)),
        'RIGHT': (row, min(col + 1, COLS - 1))
    }
    return transitions[action]

def value_iteration() -> np.ndarray:
    """Performs Value Iteration to compute the optimal value function."""
    V = np.zeros((ROWS, COLS))  # Initialize values
    while True:
        delta = 0
        for row in range(ROWS):
            for col in range(COLS):
                if (row, col) == GOAL:
                    continue  # Goal state remains unchanged

                v_old = V[row, col]

                # Compute Bellman update
                V[row, col] = max(
                    ACTION_PROB * (
                        REWARD_GOAL if get_next_state((row, col), action) == GOAL else REWARD_OTHER + GAMMA * V[get_next_state((row, col), action)]
                    ) for action in ACTIONS
                )

                delta = max(delta, abs(v_old - V[row, col]))  # Track convergence
        if delta < THRESHOLD:
            break  # Stop when convergence threshold is met
    return V

def extract_policy(V: np.ndarray) -> np.ndarray:
    """Extracts the optimal policy from the computed value function."""
    policy = np.full((ROWS, COLS), ' ', dtype=str)
    for row in range(ROWS):
        for col in range(COLS):
            if (row, col) == GOAL:
                policy[row, col] = 'G'  # Goal state marker
                continue

            # Find the best action
            best_action = max(ACTIONS, key=lambda action: REWARD_GOAL if get_next_state((row, col), action) == GOAL else REWARD_OTHER + GAMMA * V[get_next_state((row, col), action)])
            policy[row, col] = best_action[0]  # Store the first letter of the best action
    return policy

def main() -> None:
    """Runs Value Iteration and extracts the optimal policy."""
    V = value_iteration()
    policy = extract_policy(V)

    print("\nOptimal Value Function\n")
    print(np.round(V, 2))
    print("\nOptimal Policy\n")
    print(policy)

if __name__ == "__main__":
    main()