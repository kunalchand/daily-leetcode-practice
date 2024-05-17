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


# https://leetcode.com/problems/path-with-minimum-effort/
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows = len(heights)
        cols = len(heights[0])

        effort = float("-inf")

        visited = set()
        minHeap = []

        visited.add((0, 0))
        heapq.heappush(minHeap, (0, 0, 0))

        while True:
            e, x, y = heapq.heappop(minHeap)

            visited.add((x, y))
            effort = max(effort, e)

            if x == rows - 1 and y == cols - 1:
                return effort

            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if (
                    (0 <= x + dx < rows)
                    and (0 <= y + dy < cols)
                    and (x + dx, y + dy) not in visited
                ):
                    heapq.heappush(
                        minHeap,
                        (abs(heights[x][y] - heights[x + dx][y + dy]), x + dx, y + dy),
                    )
