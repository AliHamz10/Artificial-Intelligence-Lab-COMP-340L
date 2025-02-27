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

# Reflex Agent for Vacuum Cleaner World Problem

def goal_test(state):
    return all(status == 0 for status in state.values())


def clean(room, state, actions, path_cost):
    print(f"Cleaning room {room}...")
    state[room] = 0
    actions.append(f"Clean {room}")
    return path_cost + 1


def move_to_next_room(current_room):
    room_order = ["A", "B", "C"]
    index = room_order.index(current_room)
    return room_order[index + 1] if index < len(room_order) - 1 else None


def vacuum_cleaner_agent(initial_location, state):
    current_room = initial_location
    actions = []
    path_cost = 0

    while not goal_test(state):
        if state[current_room] == 1:
            path_cost = clean(current_room, state, actions, path_cost)
        next_room = move_to_next_room(current_room)
        if next_room:
            actions.append(f"Move to {next_room}")
            path_cost += 1
            current_room = next_room
        else:
            break

    return actions, path_cost


def get_user_input():
    valid_rooms = {"A", "B", "C"}

    while True:
        initial_location = input("Enter initial location (A/B/C): ").strip().upper()
        if initial_location in valid_rooms:
            break
        print("Invalid input! Please enter A, B, or C.")

    def validate_room_input(room_name):
        while True:
            try:
                status = int(input(f"Enter status of room {room_name} (0 for clean, 1 for dirty): ").strip())
                if status in {0, 1}:
                    return status
                else:
                    print("Invalid input! Please enter 0 or 1.")
            except ValueError:
                print("Invalid input! Please enter a numerical value (0 or 1).")

    return initial_location, {room: validate_room_input(room) for room in ["A", "B", "C"]}


def display_results(actions, path_cost):
    print("\nSequence of Actions:")
    for action in actions:
        print(action)
    print(f"\nTotal Path Cost: {path_cost}")


if __name__ == "__main__":
    initial_location, state = get_user_input()
    actions, path_cost = vacuum_cleaner_agent(initial_location, state)
    display_results(actions, path_cost)