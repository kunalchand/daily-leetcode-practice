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
    # BFS Add Water Layer Approach Time-O(m*n)
    """
    def addWaterLayer(self, grid:List[List[str]]) -> None:
        grid.append(["0"] * (self.n))
        grid.insert(0, ["0"] * (self.n))

        for row in grid:
            row.append("0")
            row.insert(0, "0")

    def BFS(self, grid:List[List[str]]) -> None:
        visited = set()
        queue = deque()

        for i in range(self.m + 2):
            for j in range(self.n + 2):
                if grid[i][j] == "1" and (i,j) not in visited:
                    self.islandCount += 1

                    visited.add((i,j))
                    queue.append((i,j))

                    while queue:
                        x, y = queue.popleft()

                        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                        for dx, dy in directions:
                            if (x+dx, y+dy) not in visited and grid[x+dx][y+dy] == "1":
                                visited.add((x+dx, y+dy))
                                queue.append((x+dx, y+dy))

    def numIslands(self, grid: List[List[str]]) -> int:
        self.m = len(grid)
        self.n = len(grid[0])

        self.addWaterLayer(grid)

        self.islandCount = 0

        self.BFS(grid)

        return self.islandCount
    """

    # BFS Boundary Check Approach Time-O(m*n)
    """
    def BFS(self, grid: List[List[str]]) -> None:
        visited = set()
        queue = deque()

        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == "1" and (i, j) not in visited:
                    self.islandCount += 1

                    visited.add((i, j))
                    queue.append((i, j))

                    while queue:
                        x, y = queue.popleft()

                        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                        for dx, dy in directions:
                            if (
                                (0 <= x + dx < self.m)
                                and (0 <= y + dy < self.n)
                                and (x + dx, y + dy) not in visited
                                and grid[x + dx][y + dy] == "1"
                            ):
                                visited.add((x + dx, y + dy))
                                queue.append((x + dx, y + dy))

    def numIslands(self, grid: List[List[str]]) -> int:
        self.m = len(grid)
        self.n = len(grid[0])

        self.islandCount = 0

        self.BFS(grid)

        return self.islandCount
    """

    # DFS Recursive, Boundary Check Approach Time-O(m*n)
    def DFS(self, grid: List[List[int]], x: int, y: int) -> None:
        if (
            not (0 <= x < self.m)
            or not (0 <= y < self.n)
            or grid[x][y] == "0"
            or (x, y) in self.visited
        ):
            return
        else:
            self.visited.add((x, y))

            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                self.DFS(grid, x + dx, y + dy)

    def numIslands(self, grid: List[List[str]]) -> int:
        self.m = len(grid)
        self.n = len(grid[0])

        self.visited = set()
        islandCount = 0

        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == "1" and (i, j) not in self.visited:
                    self.DFS(grid, i, j)
                    islandCount += 1

        return islandCount


print(
    Solution().numIslands(
        [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"],
        ]
    )
)

print(
    Solution().numIslands(
        [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"],
        ]
    )
)
