import math
from typing import List, Tuple

# Constants for players and empty spaces
PLAYER_X = 'X'  # Computer
PLAYER_O = 'O'  # Human
EMPTY = ' '


def print_board(board: List[List[str]]) -> None:
    for row in board:
        print(" | ".join(row))
    print("-" * 9)


def is_moves_left(board: List[List[str]]) -> bool:
    return any(cell == EMPTY for row in board for cell in row)


def evaluate(board: List[List[str]]) -> int:
    # Check rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != EMPTY:
            return 10 if board[i][0] == PLAYER_X else -10
        if board[0][i] == board[1][i] == board[2][i] != EMPTY:
            return 10 if board[0][i] == PLAYER_X else -10

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return 10 if board[0][0] == PLAYER_X else -10
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return 10 if board[0][2] == PLAYER_X else -10

    return 0


def minimize(board: List[List[str]], alpha: int, beta: int) -> int:
    score = evaluate(board)
    if score in {10, -10}:
        return score
    if not is_moves_left(board):
        return 0

    best = math.inf
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                board[i][j] = PLAYER_O
                best = min(best, maximize(board, alpha, beta))
                board[i][j] = EMPTY
                beta = min(beta, best)
                if beta <= alpha:
                    return best
    return best


def maximize(board: List[List[str]], alpha: int, beta: int) -> int:
    score = evaluate(board)
    if score in {10, -10}:
        return score
    if not is_moves_left(board):
        return 0

    best = -math.inf
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                board[i][j] = PLAYER_X
                best = max(best, minimize(board, alpha, beta))
                board[i][j] = EMPTY
                alpha = max(alpha, best)
                if beta <= alpha:
                    return best
    return best


def get_best_move(board: List[List[str]]) -> Tuple[int, int]:
    best_value = -math.inf
    best_move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                board[i][j] = PLAYER_X
                move_value = minimize(board, -math.inf, math.inf)
                board[i][j] = EMPTY

                if move_value > best_value:
                    best_value = move_value
                    best_move = (i, j)

    return best_move


def play_game():
    board = [[EMPTY for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe! You are 'O' and the computer is 'X'.")

    while True:
        print_board(board)
        if evaluate(board) == 10:
            print("Computer wins! 😎")
            break
        elif evaluate(board) == -10:
            print("You win! 🎉")
            break
        elif not is_moves_left(board):
            print("It's a draw! 🤝")
            break

        # Human move
        row, col = -1, -1
        while True:
            try:
                row, col = map(int, input("Enter your move (row and column, e.g. 0 2): ").split())
                if board[row][col] == EMPTY:
                    break
                else:
                    print("That spot is already taken. Try again.")
            except (ValueError, IndexError):
                print("Invalid input. Enter row and column as two numbers between 0 and 2.")

        board[row][col] = PLAYER_O
        print_board(board)
        if evaluate(board) == -10:
            print("You win! 🎉")
            break

        # Computer move
        if is_moves_left(board):
            print("Computer is thinking...")
            best_move = get_best_move(board)
            board[best_move[0]][best_move[1]] = PLAYER_X


def main():
    play_game()


if __name__ == "__main__":
    main()