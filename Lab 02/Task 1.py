"""
Reflex Agent Program for Vacuum Cleaner World Problem

States:
A, B, and C represent the rooms. Each room can be either clean (0) or dirty (1).
The agent will perform actions in these rooms to reach a goal state.

Goal State:
The goal state is when all rooms (A, B, and C) are clean, i.e., {"A": 0, "B": 0, "C": 0}

Actions:
0: CLEAN (clean the current room if it's dirty)
1: DIRTY (move to the next room if the current room is clean)

States Sequence:
A -> B -> C are rooms connected in this order. The agent can move from one room to another.
The agent starts in a given room (A/B/C) and moves through the rooms in sequence A -> B -> C.

Path Cost:
The path cost is +1 for every action performed (either cleaning or moving from one room to another).

Inputs:
1. LOCATION: The initial location of the vacuum cleaner (A, B, or C).
2. Status of the current room: (0 for clean, 1 for dirty).
3. Status of the other rooms: Status of rooms A, B, and C (0 for clean, 1 for dirty).

Output:
The program returns a sequence of actions that leads to the goal state, where all rooms are clean.
It also outputs the path cost, which is the total number of actions taken by the agent.

Agent's Behavior:
- If the current room is dirty, the agent will clean it (Action: 0).
- If the current room is clean, the agent will move to the next room in the sequence (Action: 1).
- The agent senses the status of other rooms before performing any action, so it knows if it needs to move or clean.

Goal Test:
The agent keeps performing actions until all rooms (A, B, and C) are clean, i.e., the state becomes {"A": 0, "B": 0, "C": 0}.

The agent's task is to clean the rooms and then report the sequence of actions it performed to reach the goal state, along with the total path cost.
"""

# Reflex Agent Program for Vacuum Cleaner World Problem

# Goal State: When all rooms are clean (i.e., {"A": 0, "B": 0, "C": 0})
goal_state = {"A": 0, "B": 0, "C": 0}


# Function to check if the goal state is achieved
def goal_test(state):
    return state == goal_state


# Function to clean a room (sets room status to clean, i.e., 0)
def clean(room, state):
    print(f"Cleaning room {room}...")
    state[room] = 0
    return state


# Function to move to the next room
def move_to_next_room(current_room):
    if current_room == "A":
        return "B"
    elif current_room == "B":
        return "C"
    else:
        return None  # No more rooms after C


# Function to handle the agent's behavior based on its location and room status
def agent_perform_action(current_room, state, actions, path_cost):
    if state[current_room] == 1:  # If current room is dirty
        state = clean(current_room, state)
        actions.append(f"Clean {current_room}")
        path_cost += 1  # Cleaning action adds 1 to path cost
    else:
        next_room = move_to_next_room(current_room)
        if next_room:
            actions.append(f"Move to {next_room}")
            path_cost += 1  # Moving to the next room adds 1 to path cost
        current_room = next_room
    return current_room, state, actions, path_cost


# Function to get the status of rooms from the user
def get_user_input():
    initial_location = input("Enter initial location (A/B/C): ").strip().upper()
    status_A = int(input("Enter status of room A (0 for clean, 1 for dirty): "))
    status_B = int(input("Enter status of room B (0 for clean, 1 for dirty): "))
    status_C = int(input("Enter status of room C (0 for clean, 1 for dirty): "))
    return initial_location, [status_A, status_B, status_C]


# Main function to execute the vacuum cleaner agent's task
def vacuum_cleaner_agent(initial_location, status):
    # Initialize state based on input
    state = {"A": status[0], "B": status[1], "C": status[2]}

    current_location = initial_location
    actions = []
    path_cost = 0

    # Continue cleaning until the goal state is reached
    while not goal_test(state):
        current_location, state, actions, path_cost = agent_perform_action(
            current_location, state, actions, path_cost
        )

    # Return the sequence of actions and total path cost
    return actions, path_cost


# Function to display the results of the agent's actions
def display_results(actions, path_cost):
    print("\nSequence of Actions:")
    for action in actions:
        print(action)

    print(f"\nTotal Path Cost: {path_cost}")


# Main driver function
if __name__ == "__main__":
    initial_location, status = get_user_input()

    # Run the vacuum cleaner agent
    actions, path_cost = vacuum_cleaner_agent(initial_location, status)

    # Display the results
    display_results(actions, path_cost)