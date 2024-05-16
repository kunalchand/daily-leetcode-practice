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


# https://leetcode.com/problems/find-the-safest-path-in-a-grid/
class Solution:
    def generateDistance(self, grid: List[List[int]]) -> None:
        for row in range(self.n):
            for col in range(self.n):
                if grid[row][col] == 1:
                    self.visited.add((row, col))
                    self.queue.append((row, col, 0))

        while self.queue:
            x, y, level = self.queue.popleft()

            for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                if (
                    (0 <= x + dx < self.n)
                    and (0 <= y + dy < self.n)
                    and (x + dx, y + dy) not in self.visited
                ):
                    self.distance[x + dx][y + dy] = level + 1
                    self.visited.add((x + dx, y + dy))
                    self.queue.append((x + dx, y + dy, level + 1))

    def modifiedDijkstra(self) -> None:
        maxHeap = []

        self.visited.add((0, 0))
        heapq.heappush(maxHeap, (-self.distance[0][0], 0, 0))

        while True:
            d, x, y = heapq.heappop(maxHeap)

            self.safeness = min(self.safeness, -d)

            if x == self.n - 1 and y == self.n - 1:
                return

            for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                if (
                    (0 <= x + dx < self.n)
                    and (0 <= y + dy < self.n)
                    and (x + dx, y + dy) not in self.visited
                ):
                    self.visited.add((x + dx, y + dy))
                    heapq.heappush(
                        maxHeap, (-self.distance[x + dx][y + dy], x + dx, y + dy)
                    )

    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        self.n = len(grid)

        self.distance = [[0] * self.n for _ in range(self.n)]

        self.visited = set()
        self.queue = deque()
        self.generateDistance(grid)

        self.safeness = float("inf")
        self.visited = set()
        self.modifiedDijkstra()

        return self.safeness
