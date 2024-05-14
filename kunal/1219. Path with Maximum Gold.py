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


# https://leetcode.com/problems/path-with-maximum-gold/
class Solution:
    def DFS(self, grid: List[List[int]], x: int, y: int, currentGold: int) -> None:
        if (
            not (0 <= x < self.m)
            or not (0 <= y < self.n)
            or grid[x][y] == 0
            or (x, y) in self.visited
        ):
            self.maxGold = max(self.maxGold, currentGold)
            return
        else:
            self.visited.add((x, y))
            for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                self.DFS(grid, x + dx, y + dy, currentGold + grid[x][y])
            self.visited.remove((x, y))
            return

    def getMaximumGold(self, grid: List[List[int]]) -> int:
        self.m = len(grid)
        self.n = len(grid[0])

        self.maxGold = 0

        for row in range(self.m):
            for col in range(self.n):
                if grid[row][col] != 0:
                    self.visited = set()
                    self.DFS(grid, row, col, 0)

        return self.maxGold
