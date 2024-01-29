#!/usr/bin/python3
"""The N-queens puzzle"""

import sys


def initialize_board(size):
    """Initialize an `size`x`size` sized chessboard with 0's."""
    board = [[' ' for _ in range(size)] for _ in range(size)]
    return board


def deep_copy_board(board):
    """Return a deepcopy of a chessboard."""
    if isinstance(board, list):
        return list(map(deep_copy_board, board))
    return board


def get_solution_coordinates(board):
    """Return the list of lists representation of queens' positions on a board."""
    solution = [[r, c] for r in range(len(board)) for c in range(len(board)) if board[r][c] == "Q"]
    return solution


def mark_attacked_positions(board, row, col):
    """Mark attacked positions on a chessboard."""
    for c in range(col + 1, len(board)):
        board[row][c] = "x"  # X out all forward spots
    for c in range(col - 1, -1, -1):
        board[row][c] = "x"  # X out all backward spots
    for r in range(row + 1, len(board)):
        board[r][col] = "x"  # X out all spots below
    for r in range(row - 1, -1, -1):
        board[r][col] = "x"  # X out all spots above

    # X out all spots diagonally down to the right
    c = col + 1
    for r in range(row + 1, len(board)):
        if c >= len(board):
            break
        board[r][c] = "x"
        c += 1

    # X out all spots diagonally up to the left
    c = col - 1
    for r in range(row - 1, -1, -1):
        if c < 0:
            break
        board[r][c] = "x"
        c -= 1

    # X out all spots diagonally up to the right
    c = col + 1
    for r in range(row - 1, -1, -1):
        if c >= len(board):
            break
        board[r][c] = "x"
        c += 1

    # X out all spots diagonally down to the left
    c = col - 1
    for r in range(row + 1, len(board)):
        if c < 0:
            break
        board[r][c] = "x"
        c -= 1


def recursive_solve(board, row, queens, solutions):
    """Recursively solve an N-queens puzzle."""
    if queens == len(board):
        solutions.append(get_solution_coordinates(board))
        return solutions

    for col in range(len(board)):
        if board[row][col] == " ":
            tmp_board = deep_copy_board(board)
            tmp_board[row][col] = "Q"
            mark_attacked_positions(tmp_board, row, col)
            solutions = recursive_solve(tmp_board, row + 1, queens + 1, solutions)

    return solutions


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    board_size = int(sys.argv[1])
    chessboard = initialize_board(board_size)
    solutions_found = recursive_solve(chessboard, 0, 0, [])

    for solution in solutions_found:
        print(solution)
