# Artificial-Intelligence-Lab-COMP-340L

This repository contains the complete lab work for the Artificial Intelligence course (COMP-340L). It includes 10 comprehensive labs covering fundamental AI concepts, algorithms, and implementations.

## Course Overview

This course provides hands-on experience with various artificial intelligence techniques including search algorithms, game theory, optimization methods, and machine learning concepts. Each lab builds upon previous knowledge and introduces new AI methodologies.

## Repository Structure

```
├── Lab 01/          # Python Fundamentals & NumPy
├── Lab 02/          # Reflex Agents
├── Lab 03/          # Iterative Deepening Search
├── Lab 04/          # A* Search Algorithm
├── Lab 05/          # Minimax Algorithm
├── Lab 06/          # Alpha-Beta Pruning
├── Lab 07/          # Expectimax Algorithm
├── Lab 08/          # Monte Carlo Tree Search
├── Lab 09/          # Hill Climbing Algorithm
├── Lab 10/          # Beam Search Algorithm
├── Lab Manuals/     # PDF manuals for each lab
├── Lab Reports/     # Lab report submissions
└── README.md        # This file
```

## Lab Descriptions

### Lab 01 - Python Fundamentals & NumPy Operations

In Lab 01, I worked on various tasks involving dictionary manipulation, looping with lists and dictionaries, and NumPy array manipulation. I created and updated dictionaries to represent student information and inventory items, used for loops and while loops to iterate through lists and dictionaries, and performed operations such as adding new subjects, updating ages, and printing personalized messages. Additionally, I manipulated NumPy arrays by calculating statistical measures, reshaping arrays, performing matrix multiplication, and filtering values based on a threshold.

### Lab 02 - Reflex Agent Implementation

In Lab 02, I implemented a Reflex Agent Program for the Vacuum Cleaner World Problem. The agent's goal is to clean all rooms (A, B, and C) by performing actions such as cleaning the current room or moving to the next room. The program includes functions to check the goal state, clean rooms, move between rooms, and handle the agent's behavior based on the room's status. The agent's task is to clean the rooms and report the sequence of actions performed to reach the goal state, along with the total path cost.

### Lab 03 - Iterative Deepening Depth-First Search

In Lab 03, I implemented a solution to the 8-puzzle problem using the Iterative Deepening Depth-First Search (IDDFS) algorithm. This approach combines the space efficiency of depth-first search with the optimality guarantees of breadth-first search by progressively increasing the depth limit until a solution is found.

### Lab 04 - A* Search Algorithm

In Lab 04 of the Artificial Intelligence course, I implemented the A* Search Algorithm to find the shortest path in a grid with obstacles, using the Manhattan distance heuristic. The lab consisted of two tasks: the first involved implementing A* to determine its completeness and optimality, while the second required applying A* to both unweighted and weighted graphs, comparing its efficiency with BFS and analyzing its suitability for weighted graphs. The implementation included writing Python code for both graph types and providing observations on when to use A* effectively.

### Lab 05 - Minimax Algorithm for Game Playing

In this lab, we implemented the Minimax Algorithm for Tic-Tac-Toe, optimizing decision-making using adversarial search. The task involved coding minimax, testing game outcomes, and documenting the approach in a Jupyter Notebook. The implementation demonstrates how the algorithm explores the game tree to find optimal moves by assuming both players play optimally.

### Lab 06 - Alpha-Beta Pruning Optimization

In Lab 06, I implemented the Alpha-Beta Pruning Algorithm for Tic-Tac-Toe, enhancing the Minimax Algorithm's efficiency by reducing the search space. The lab required coding the alpha-beta pruning algorithm, testing game outcomes, and comparing the results with the Minimax Algorithm. This optimization technique significantly improves performance by eliminating branches that cannot possibly influence the final decision.

### Lab 07 - Expectimax Algorithm for Probabilistic Games

In Lab 07, I implemented the Expectimax Algorithm for Tic-Tac-Toe, extending the Minimax Algorithm to handle probabilistic outcomes. The lab involved coding the Expectimax Algorithm, testing game outcomes, and documenting the approach in a Jupyter Notebook. The implementation included handling chance nodes and evaluating expected values for optimal decision-making in uncertain scenarios.

### Lab 08 - Monte Carlo Tree Search

In Lab 08, I implemented the Monte Carlo Tree Search (MCTS) algorithm for Tic-Tac-Toe, focusing on decision-making in uncertain environments. The lab involved coding the MCTS algorithm, testing game outcomes, and documenting the approach in a Jupyter Notebook. The implementation included simulating random games to evaluate potential moves and selecting the best action based on the results of these simulations.

### Lab 09 - Hill Climbing Algorithm

In Lab 09, I implemented the Hill Climbing Algorithm for pathfinding problems. This lab focused on local search techniques where the algorithm makes decisions based on improving the current state by moving to neighboring states with better evaluation scores. The implementation included two main tasks:

- **Task 01**: Basic Hill Climbing implementation for maze navigation using Manhattan distance heuristic
- **Task 02**: Hill Climbing with Random Restarts to overcome local maxima problems

The lab demonstrated both the strengths and limitations of hill climbing, particularly its tendency to get stuck in local optima and how random restarts can help mitigate this issue.

### Lab 10 - Beam Search Algorithm

In Lab 10, I implemented the Beam Search Algorithm, which is a heuristic search algorithm that explores a graph by expanding the most promising nodes in a limited set. The lab included two primary implementations:

- **Task 01**: Beam Search for pathfinding in weighted grids, maintaining only the best k paths at each level
- **Task 02**: Beam Search applied to the 8-puzzle problem using Manhattan distance heuristic

This algorithm represents a compromise between the optimality of breadth-first search and the memory efficiency of depth-first search by keeping only a limited number of the best candidates at each step.

## Key Learning Outcomes

Through these labs, I have gained practical experience in:

- **Search Algorithms**: Implementing various search strategies from uninformed (BFS, DFS, IDDFS) to informed search (A*, Hill Climbing, Beam Search)
- **Game Theory**: Understanding adversarial search through Minimax, Alpha-Beta Pruning, and Expectimax algorithms
- **Optimization Techniques**: Learning about local search methods and their applications in problem-solving
- **Probabilistic Decision Making**: Implementing algorithms that handle uncertainty and randomness
- **Algorithm Analysis**: Comparing performance, completeness, and optimality of different approaches

## Technical Skills Developed

- **Python Programming**: Advanced Python concepts including classes, data structures, and algorithm implementation
- **NumPy**: Mathematical operations and array manipulations for AI computations
- **Algorithm Design**: Implementing complex search and optimization algorithms from scratch
- **Performance Analysis**: Evaluating algorithm efficiency and comparing different approaches
- **Problem Solving**: Applying AI techniques to solve real-world problems

## Requirements

- Python 3.7 or higher
- NumPy library
- Jupyter Notebook (for some labs)
- Basic understanding of Python programming concepts

## Installation & Setup

1. Clone this repository:
   ```bash
   git clone [repository-url]
   cd Artificial-Intelligence-Lab-COMP-340L
   ```

2. Install required dependencies:
   ```bash
   pip install numpy jupyter
   ```

3. Navigate to any lab directory and run the Python files:
   ```bash
   cd "Lab 01"
   python [filename].py
   ```

## Usage

Each lab directory contains:
- Python implementation files
- Input/test data (where applicable)
- Documentation and comments explaining the algorithms

To run a specific lab:
1. Navigate to the lab directory
2. Read the corresponding lab manual in `Lab Manuals/` for detailed instructions
3. Execute the Python files to see the algorithms in action
4. Review the lab reports in `Lab Reports/` for detailed analysis and results

## Documentation

- **Lab Manuals**: Detailed instructions and theoretical background for each lab
- **Lab Reports**: Comprehensive analysis, results, and conclusions for each implementation
- **Code Comments**: Inline documentation explaining algorithm logic and implementation details

## Assessment & Results

All labs have been completed successfully with comprehensive implementations and thorough testing. The repository demonstrates a solid understanding of artificial intelligence concepts and their practical applications.

## Acknowledgments

This work was completed as part of the COMP-340L Artificial Intelligence Lab course. Special thanks to the course instructors for providing comprehensive lab manuals and guidance throughout the learning process.

## Contact Information

For questions or clarifications about any of the implementations, please refer to the lab reports or contact through the appropriate course channels.

---

*This repository represents a comprehensive journey through fundamental artificial intelligence algorithms and techniques, providing both theoretical understanding and practical implementation experience.*

