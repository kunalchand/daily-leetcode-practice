import copy
import heapq
import math
import random
from collections import Counter, defaultdict, deque
from dataclasses import dataclass
from functools import cmp_to_key, reduce
from itertools import zip_longest
from math import factorial, sqrt
from typing import Dict, List, Optional, Tuple, Union


class Point:
    def __init__(self, x: int, y: int) -> None:
        self.location = [x, y]
        self.distance = math.sqrt(x**2 + y**2)

    def __lt__(self, other) -> bool:
        return self.distance < other.distance

    def __repr__(self) -> str:
        return "(" + str(self.location) + " -> " + str(self.distance) + ")"


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []

        for x, y in points:
            heapq.heappush(minHeap, Point(x, y))

        ans = []
        for _ in range(k):
            ans.append(heapq.heappop(minHeap).location)

        return ans


print(Solution().kClosest([[1, 3], [-2, 2]], 1))
print(Solution().kClosest([[3, 3], [5, -1], [-2, 4]], 2))
