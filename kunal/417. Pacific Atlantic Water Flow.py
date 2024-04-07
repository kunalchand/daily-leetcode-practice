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
    # DFS Approach, Time-O(m*n) Space-O(m*n)
    """
    def DFS(self, heights: List[List[int]], x: int, y: int, ocean: str) -> None:
        self.visited.add((x, y))
        self.waterType[x][y].add(ocean)

        for dx, dy in [(1,0), (-1, 0), (0, 1), (0, -1)]:
            if x+dx in range(self.m) and y+dy in range(self.n) and heights[x][y] <= heights[x+dx][y+dy] and (x+dx, y+dy) not in self.visited:
                self.DFS(heights, x+dx, y+dy, ocean)

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        self.m = len(heights)
        self.n = len(heights[0])

        self.waterType = [[set() for _ in range(self.n)] for _ in range(self.m)]

        # Pacific
        self.visited = set()

        for x in range(self.m):
            self.DFS(heights, x, 0, "Pacific")

        for y in range(self.n):
            self.DFS(heights, 0, y, "Pacific")

        # Atlantic
        self.visited = set()

        for x in range(self.m):
            self.DFS(heights, x, self.n-1, "Atlantic")

        for y in range(self.n):
            self.DFS(heights, self.m-1, y, "Atlantic")

        ans = []
        for x in range(self.m):
            for y in range(self.n):
                if "Pacific" in self.waterType[x][y] and "Atlantic" in self.waterType[x][y]:
                    ans.append([x, y])

        return ans
    """

    # BFS Approach, Time-O(m*n) Space-O(m*n)
    def BFS(self, heights: List[List[int]], i: int, j: int, ocean: str) -> None:
        self.visited.add((i, j))
        self.waterType[i][j].add(ocean)
        self.queue.append((i, j))

        while self.queue:
            x, y = self.queue.popleft()

            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if (
                    x + dx in range(self.m)
                    and y + dy in range(self.n)
                    and heights[x][y] <= heights[x + dx][y + dy]
                    and (x + dx, y + dy) not in self.visited
                ):
                    self.visited.add((x + dx, y + dy))
                    self.waterType[x + dx][y + dy].add(ocean)
                    self.queue.append((x + dx, y + dy))

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        self.m = len(heights)
        self.n = len(heights[0])

        self.waterType = [[set() for _ in range(self.n)] for _ in range(self.m)]
        self.queue = deque()

        # Pacific
        self.visited = set()

        for x in range(self.m):
            self.BFS(heights, x, 0, "Pacific")

        for y in range(self.n):
            self.BFS(heights, 0, y, "Pacific")

        # Atlantic
        self.visited = set()

        for x in range(self.m):
            self.BFS(heights, x, self.n - 1, "Atlantic")

        for y in range(self.n):
            self.BFS(heights, self.m - 1, y, "Atlantic")

        ans = []
        for x in range(self.m):
            for y in range(self.n):
                if (
                    "Pacific" in self.waterType[x][y]
                    and "Atlantic" in self.waterType[x][y]
                ):
                    ans.append([x, y])

        return ans


print(
    Solution().pacificAtlantic(
        [
            [1, 2, 2, 3, 5],
            [3, 2, 3, 4, 4],
            [2, 4, 5, 3, 1],
            [6, 7, 1, 4, 5],
            [5, 1, 1, 2, 4],
        ]
    )
)

print(Solution().pacificAtlantic([[1]]))
