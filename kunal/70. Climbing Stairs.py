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


class Solution:
    # Recursion, Time-O(?) Space-O(1)
    """
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2

        return self.climbStairs(n-1) + self.climbStairs(n-2)
    """

    # Top Down Memoization, Time-O(n) Space-O(n)
    """
    def topDown(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2

        if n-1 not in self.memo:
            self.memo[n-1] = self.topDown(n-1)

        if n-2 not in self.memo:
            self.memo[n-2] = self.topDown(n-2)
        
        return self.memo[n-1] + self.memo[n-2]

    def climbStairs(self, n: int) -> int:
        self.memo = {}

        return self.topDown(n)
    """

    # Bottom Up Tabulation, Time-O(n) Space-O(n)
    """
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2

        dp = [0] * (n+1)

        dp[1] = 1
        dp[2] = 2

        for index in range(3, n+1):
            dp[index] = dp[index-1] + dp[index-2]
        
        return dp[n]
    """

    # Bottom Up Tabulation, Time-O(n) Space-O(1)
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2

        n_minus_two = 1
        n_minus_one = 2

        dp = -1

        for _ in range(3, n + 1):
            dp = n_minus_one + n_minus_two
            n_minus_two = n_minus_one
            n_minus_one = dp

        return dp


print(Solution().climbStairs(2))
print(Solution().climbStairs(3))
