#!/usr/bin/python3
from sys import argv

"""
Module soln for The N Queens Puzzle
"""

class Queen:
    """
    class Queen to solve nQueens problem
    """
    def can_move(self, x, y, right):
        """
        Checking if queen can move in the valid constraint column given
        """
        for a in range(x):
            if right[a] == y:
                return (False)
            if abs(right[a] - y) == (x - a):
                return (False)
            return (True)

    def soln(self, n, N, right):
        """
        Finding all the right combos that can happen using recursion
        """
        if n == N:
            print("[", end="")
            for j in range(N):
                print("{}, {}]".format(j, right[j]), end="")
                if j < N - 1:
                    print(", ", end="")
            print("]")
            return

        for j in range(N):
            if self.can_move(n, j, right):
                right[n] = j
                self.solution(n + 1, N, right)

if __name__ == "__main__":
    count = len(argv)

    if count != 2:
        print("Usage: nqueens N")
        exit(1)
    else:
        try:
            N = int(arg[1])
        except:
            print("N must be a number")
            exit(1)
    if N < 4:
        print("N must be at least 4")
        exit(1)

    final = Queen()
    final.soln(0, N, [None for i in range(N)])
