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


# https://leetcode.com/problems/largest-local-values-in-a-matrix/
class Solution:
    # Time-O(n^2) Space-O(n^2)
    def fillMax(self, grid: List[List[int]], row: int, col: int) -> None:
        for i in range(row, row + 3):
            for j in range(col, col + 3):
                self.ans[row][col] = max(self.ans[row][col], grid[i][j])

    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)

        self.ans = [[-1 for _ in range(n - 2)] for _ in range(n - 2)]

        for row in range(0, n - 2):
            for col in range(0, n - 2):
                self.fillMax(grid, row, col)

        return self.ans


print(Solution().largestLocal([[9, 9, 8, 1], [5, 6, 2, 6], [8, 2, 6, 4], [6, 2, 2, 2]]))
