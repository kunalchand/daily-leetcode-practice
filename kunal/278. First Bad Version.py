import bisect
import copy
import heapq
import math
import random
from bisect import bisect, bisect_left, bisect_right, insort, insort_left, insort_right
from collections import Counter, defaultdict, deque
from dataclasses import dataclass
from functools import cache, cmp_to_key, lru_cache, reduce
from heapq import heapify, heappop, heappush, heappushpop
from itertools import combinations, pairwise, permutations, zip_longest
from math import ceil, factorial, floor, inf, sqrt
from typing import Deque, Dict, List, Optional, Set, Tuple, Union


# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    pass


# https://leetcode.com/problems/first-bad-version/
class Solution:
    # Iterative
    """
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n

        first_bad_version = n+1

        while left <= right:
            mid = left + (right - left) // 2

            if isBadVersion(mid):
                first_bad_version = mid
                right = mid - 1
            else:
                left = mid + 1

        return first_bad_version
    """

    # Recursive
    def binarySearch(self, start: int, end: int) -> None:
        if start > end:
            return
        else:
            mid = (start + end) // 2

            if isBadVersion(mid):
                self.badVersion = mid
                self.binarySearch(start, mid - 1)
            else:
                self.binarySearch(mid + 1, end)

    def firstBadVersion(self, n: int) -> int:
        self.badVersion = n + 1
        self.binarySearch(1, n)
        return self.badVersion
