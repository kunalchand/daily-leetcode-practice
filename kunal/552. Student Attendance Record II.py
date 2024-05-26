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


# https://leetcode.com/problems/student-attendance-record-ii/
class Solution:
    # Recursion (TLE)
    """
    def ways(self, n: int, A: int, L: int) -> int:
        if n == 0:
            return 1
        else:
            records = 0
            # Take A and reset consecutive L
            if A > 0:
                records += self.ways(n-1, A-1, 2)
            # Take L and keep track of consecutive L
            if L > 0:
                records += self.ways(n-1, A, L-1)
            # Take P and reset consecutive L
            records += self.ways(n-1, A, 2)

            records %= 1000000007

            return records


    def checkRecord(self, n: int) -> int:
        return self.ways(n, 1, 2)
    """

    # DP, Top Down Memoization
    def ways(self, n: int, A: int, L: int) -> int:
        if (n, A, L) in self.memo:
            return self.memo[(n, A, L)]
        if n == 0:
            return 1
        else:
            records = 0
            # Take A and reset consecutive L
            if A > 0:
                records += self.ways(n - 1, A - 1, 2)
            # Take L and keep track of consecutive L
            if L > 0:
                records += self.ways(n - 1, A, L - 1)
            # Take P and reset consecutive L
            records += self.ways(n - 1, A, 2)

            records %= 1000000007

            self.memo[(n, A, L)] = records
            return records

    def checkRecord(self, n: int) -> int:
        self.memo = {}
        return self.ways(n, 1, 2)
