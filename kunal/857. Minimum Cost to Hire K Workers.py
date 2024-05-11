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


# https://leetcode.com/problems/minimum-cost-to-hire-k-workers/
class Solution:
    # Reference: https://www.youtube.com/watch?v=o8emK4ehhq0
    # Time-O(n*logn) Space-O(n + k)
    def mincostToHireWorkers(
        self, quality: List[int], wage: List[int], k: int
    ) -> float:
        workers = [(w / q, q, w) for q, w in zip(quality, wage)]
        workers.sort()  # O(n*logn)

        maxHeap = []
        heapSum = 0
        for index in range(k - 1):  # O(k*logk)
            r, q, w = workers[index]
            heapq.heappush(maxHeap, -q)
            heapSum += q

        money = float("inf")
        for captian in range(k - 1, len(workers)):  # O(n*logk)
            r, q, w = workers[captian]
            money = min(money, (heapSum * r) + w)

            heapq.heappush(maxHeap, -q)
            heapSum += q
            heapSum -= -maxHeap[0]
            heapq.heappop(maxHeap)

        return money
