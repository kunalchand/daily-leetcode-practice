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


# https://leetcode.com/problems/min-cost-climbing-stairs/description/
class Solution:
    # Recursion, Time-O(?) Space-O(1) (TLE)
    """
    def findCost(self, cost: List[int], n: int) -> int:
        if n == 0 or n == 1:
            return 0

        return min(self.findCost(cost, n-1) + cost[n-1], self.findCost(cost, n-2) + cost[n-2])

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        return self.findCost(cost, len(cost))
    """

    # Top Down Memoization, Time-O(n) Space-O(n)
    """
    def findCost(self, cost: List[int], n: int) -> int:
        if n == 0 or n == 1:
            return 0

        if n-1 not in self.memo:
            self.memo[n-1] = self.findCost(cost, n-1)
        if n-2 not in self.memo:
            self.memo[n-2] = self.findCost(cost, n-2)

        return min(self.memo[n-1] + cost[n-1], self.memo[n-2] + cost[n-2])

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        self.memo = {}

        return self.findCost(cost, len(cost))
    """

    # Bottom Up Tabulation, Time-O(n) Space-O(n)
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * (n + 1)

        dp[0] = 0
        dp[1] = 0

        for index in range(2, n + 1):
            dp[index] = min(
                dp[index - 1] + cost[index - 1], dp[index - 2] + cost[index - 2]
            )

        return dp[n]


print(Solution().minCostClimbingStairs([10, 15, 20]))
print(Solution().minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
