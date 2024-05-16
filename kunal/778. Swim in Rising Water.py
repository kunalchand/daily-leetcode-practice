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


# https://leetcode.com/problems/swim-in-rising-water/
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)

        time = 0

        visited = set()
        minHeap = []

        visited.add((0, 0))
        heapq.heappush(minHeap, (grid[0][0], 0, 0))

        while True:
            elevation, x, y = minHeap[0]
            if time < elevation:
                time += 1
            elif time >= elevation:
                if x == n - 1 and y == n - 1:
                    return time
                heapq.heappop(minHeap)
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    if (
                        (0 <= x + dx < n)
                        and (0 <= y + dy < n)
                        and (x + dx, y + dy) not in visited
                    ):
                        visited.add((x + dx, y + dy))
                        heapq.heappush(minHeap, (grid[x + dx][y + dy], x + dx, y + dy))
