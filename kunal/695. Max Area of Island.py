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


class Solution:
    # BFS Iterative
    """
    def BFS(self, grid: List[List[int]], x: int, y: int) -> int:
        self.queue.append((x,y))
        self.visited.add((x,y))
        count = 1

        while self.queue:
            i, j = self.queue.popleft()

            for di, dj in [(1,0), (-1,0), (0, 1), (0,-1)]:
                if (0 <= i + di < self.m) and (0 <= j + dj < self.n) and grid[i+ di][j + dj] == 1 and (i + di, j + dj) not in self.visited:
                    self.queue.append((i + di, j + dj))
                    self.visited.add((i + di, j + dj))
                    count += 1

        return count

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.m = len(grid)
        self.n = len(grid[0])

        self.largestIsland = 0
        self.visited = set()
        self.queue = deque()

        for x in range(self.m):
            for y in range(self.n):
                if grid[x][y] == 1 and (x,y) not in self.visited:
                    self.largestIsland = max(self.largestIsland, self.BFS(grid, x, y))

        return self.largestIsland
    """

    # DFS Iterative
    """
    def DFS(self, grid: List[List[int]], x: int, y: int) -> int:
        count = 0
        self.stack.append((x,y))

        while self.stack:
            i, j = self.stack.pop()
            if (0 <= i < self.m) and (0 <= j < self.n) and grid[i][j] == 1 and (i, j) not in self.visited:
                self.visited.add((i, j))
                count += 1
                for di, dj in [(1,0), (-1,0), (0, 1), (0,-1)]:
                    self.stack.append((i + di, j + dj))
        
        return count

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.m = len(grid)
        self.n = len(grid[0])

        self.largestIsland = 0
        self.visited = set()
        self.stack = []

        for x in range(self.m):
            for y in range(self.n):
                if grid[x][y] == 1 and (x,y) not in self.visited:
                    self.largestIsland = max(self.largestIsland, self.DFS(grid, x, y))

        return self.largestIsland
    """

    # DFS Recursive
    def DFS(self, grid: List[List[int]], i: int, j: int) -> int:
        if (
            (0 <= i < self.m)
            and (0 <= j < self.n)
            and grid[i][j] == 1
            and (i, j) not in self.visited
        ):
            self.visited.add((i, j))
            count = 1
            for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                count += self.DFS(grid, i + di, j + dj)
            return count
        else:
            return 0

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.m = len(grid)
        self.n = len(grid[0])

        self.largestIsland = 0
        self.visited = set()

        for x in range(self.m):
            for y in range(self.n):
                if grid[x][y] == 1 and (x, y) not in self.visited:
                    self.largestIsland = max(self.largestIsland, self.DFS(grid, x, y))

        return self.largestIsland


print(
    Solution().maxAreaOfIsland(
        [
            [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
        ]
    )
)

print(Solution().maxAreaOfIsland([[0, 0, 0, 0, 0, 0, 0, 0]]))
