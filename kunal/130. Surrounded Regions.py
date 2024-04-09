import bisect
import copy
import heapq
import math
import random
from bisect import bisect, bisect_left, bisect_right, insort, insort_left, insort_right
from collections import Counter, defaultdict, deque
from dataclasses import dataclass
from functools import cmp_to_key, reduce
from itertools import zip_longest
from math import ceil, factorial, floor, sqrt
from typing import Dict, List, Optional, Set, Tuple, Union


# https://leetcode.com/problems/surrounded-regions/description/
class Solution:
    # DFS Traversal, Time-O(m*n) Space-O(m*n)
    '''
    def DFS(self, board: List[List[str]], convert: bool, x: int, y: int) -> None:
        if x not in range(self.m) or y not in range(self.n) or board[x][y] == "X" or (x,y) in self.visited:
            return
        else:
            self.visited.add((x, y))
            if convert:
                board[x][y] = "X"

            for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                self.DFS(board, convert, x+dx, y+dy)

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.m = len(board)
        self.n = len(board[0])

        self.visited = set()

        # Border Traversal (Column)
        for x in range(self.m):
            if board[x][0] == "O":
                self.DFS(board, False, x, 0)
            if board[x][self.n-1] == "O":
                self.DFS(board, False, x, self.n-1)

        # Border Traversal (Row)
        for y in range(self.n):
            if board[0][y] == "O":
                self.DFS(board, False, 0, y)
            if board[self.m-1][y] == "O":
                self.DFS(board, False, self.m-1, y)

        # Inner Board Traversal
        for x in range(1, self.m-1):
            for y in range(1, self.n-1):
                if board[x][y] == "O":
                    self.DFS(board, True, x, y)
    '''

    # BFS Traversal, Time-O(m*n) Space-O(m*n)
    def BFS(self, board: List[List[str]], convert: bool, i: int, j: int) -> None:
        if (
            i in range(self.m)
            and j in range(self.n)
            and board[i][j] == "O"
            and (i, j) not in self.visited
        ):
            self.visited.add((i, j))
            self.queue.append((i, j))
            if convert:
                board[i][j] = "X"

        while self.queue:
            x, y = self.queue.popleft()

            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if (
                    x + dx in range(self.m)
                    and y + dy in range(self.n)
                    and board[x + dx][y + dy] == "O"
                    and (x + dx, y + dy) not in self.visited
                ):
                    self.visited.add((x + dx, y + dy))
                    self.queue.append((x + dx, y + dy))
                    if convert:
                        board[x + dx][y + dy] = "X"

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.m = len(board)
        self.n = len(board[0])

        self.visited = set()
        self.queue = deque()

        # Border Traversal (Column)
        for x in range(self.m):
            if board[x][0] == "O":
                self.BFS(board, False, x, 0)
            if board[x][self.n - 1] == "O":
                self.BFS(board, False, x, self.n - 1)

        # Border Traversal (Row)
        for y in range(self.n):
            if board[0][y] == "O":
                self.BFS(board, False, 0, y)
            if board[self.m - 1][y] == "O":
                self.BFS(board, False, self.m - 1, y)

        # Inner Board Traversal
        for x in range(1, self.m - 1):
            for y in range(1, self.n - 1):
                if board[x][y] == "O":
                    self.BFS(board, True, x, y)


board = [
    ["X", "X", "X", "X"],
    ["X", "O", "O", "X"],
    ["X", "X", "O", "X"],
    ["X", "O", "X", "X"],
]

Solution().solve(board)

print(board)

board = [["X"]]

Solution().solve(board)

print(board)
