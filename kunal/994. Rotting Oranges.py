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


# https://leetcode.com/problems/rotting-oranges/description/
class Solution:
    # Fresh to Rotten Approach, Time-O(n*m * n*m) Space-O(n*m)
    """
    def BFS(self, grid: List[List[int]], i: int, j: int) -> int:
        self.visited = set()
        self.queue = deque()

        self.visited.add((i, j))
        self.queue.append([i, j, 0])

        while self.queue:
            x, y, time = self.queue.popleft()

            # Return the time for reaching nearest Rotten Orange
            if grid[x][y] == 2:
                return time

            for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                if x+dx in range(self.m) and y+dy in range(self.n) and grid[x+dx][y+dy] != 0 and (x+dx, y+dy) not in self.visited:
                    self.visited.add((x+dx, y+dy))
                    self.queue.append([x+dx, y+dy, time + 1])

        return -1

    def orangesRotting(self, grid: List[List[int]]) -> int:
        self.m = len(grid)
        self.n = len(grid[0])

        minTime = 0

        for x in range(self.m):
            for y in range(self.n):
                # BFS on Fresh Orange
                if grid[x][y] == 1:
                    if self.BFS(grid, x, y) == -1:
                        return -1
                    else:
                        minTime = max(minTime, self.BFS(grid, x, y))

        return minTime
    """

    # Rotten to Fresh Approach, Time-O(n*m)
    def BFS(self, grid: List[List[int]]) -> int:
        self.visited = set()
        self.queue = deque()

        # Add all the rotten oranges as starting point of contamination
        for x in range(self.m):
            for y in range(self.n):
                if grid[x][y] == 2:
                    self.visited.add((x, y))
                    self.queue.append((x, y))

        time = 0

        while self.queue:
            layer = len(self.queue)

            for _ in range(layer):
                x, y = self.queue.popleft()

                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    if (
                        x + dx in range(self.m)
                        and y + dy in range(self.n)
                        and grid[x + dx][y + dy] == 1
                        and (x + dx, y + dy) not in self.visited
                    ):
                        self.visited.add((x + dx, y + dy))
                        self.queue.append((x + dx, y + dy))
                        self.freshOrangeCount -= 1

            time += 1

        # Some fresh orange remains unaffected
        if self.freshOrangeCount > 0:
            return -1
        # All fresh oranges got rotten after some time
        elif self.freshOrangeCount == 0:
            return time - 1

    def orangesRotting(self, grid: List[List[int]]) -> int:
        self.m = len(grid)
        self.n = len(grid[0])

        # Count number of Fresh Oranges
        self.freshOrangeCount = 0
        self.rottenOrangeCount = 0
        for x in range(self.m):
            for y in range(self.n):
                if grid[x][y] == 1:
                    self.freshOrangeCount += 1
                elif grid[x][y] == 2:
                    self.rottenOrangeCount += 1

        if self.freshOrangeCount == 0:
            return 0
        elif self.freshOrangeCount != 0 and self.rottenOrangeCount == 0:
            return -1
        else:
            return self.BFS(grid)


print(Solution().orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]))
print(Solution().orangesRotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]]))
print(Solution().orangesRotting([[0, 2]]))
