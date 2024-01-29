#!/usr/bin/python3
import sys

class NQueensSolver:
    def __init__(self, n):
        self.n = n
        self.board = [-1] * n

    def is_safe(self, row, col):
        for i in range(row):
            if (
                self.board[i] == col
                or self.board[i] - i == col - row
                or self.board[i] + i == col + row
            ):
                return False
        return True

    def solve_queens(self, row):
        if row == self.n:
            self.print_solution()
            return

        for col in range(self.n):
            if self.is_safe(row, col):
                self.board[row] = col
                self.solve_queens(row + 1)

    def print_solution(self):
        print("[", end="")
        for i in range(self.n):
            print("{}, ".format(self.board[i]), end="")
        print("\b\b]")

def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solver = NQueensSolver(N)
    solver.solve_queens(0)

if __name__ == "__main__":
    main()
