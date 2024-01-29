#!/usr/bin/python3
from sys import argv

class Queen:
    """
    Class to solve the N-Queens problem
    """
    def can_move(self, x, y, right):
        """
        Check if the queen can move within the valid constraint column
        """
        for a in range(x):
            if right[a] == y or abs(right[a] - y) == (x - a):
                return False
        return True

    def soln(self, n, N, right):
        """
        Find all valid combinations using recursion
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
                self.soln(n + 1, N, right)

if __name__ == "__main__":
    count = len(argv)

    if count != 2:
        print("Usage: nqueens N")
        exit(1)
    else:
        try:
            N = int(argv[1])
        except ValueError:
            print("N must be a number")
            exit(1)

    if N < 4:
        print("N must be at least 4")
        exit(1)

    final = Queen()
    final.soln(0, N, [None for _ in range(N)])
