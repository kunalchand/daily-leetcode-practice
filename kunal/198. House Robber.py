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


# https://leetcode.com/problems/house-robber/
class Solution:
    # Recursion, Time-O(?) Space-O(1) (TLE)
    """
    def moneyHeist(self, nums: List) -> int:
        if not nums:
            return 0
        else:
            # rob
            robMoney = nums[0] + self.moneyHeist(nums[2:])

            # not rob
            notRobMoney = self.moneyHeist(nums[1:])

            return max(notRobMoney, robMoney)

    def rob(self, nums: List[int]) -> int:
        return self.moneyHeist(nums)
    """

    # Top Down Memoization, Time-O(n) Space-O(n)
    """
    def moneyHeist(self, nums: List) -> int:
        if not nums:
            return 0
        else:
            robTuple = tuple(nums[2:])
            notRobTuple = tuple(nums[1:])

            if robTuple not in self.memo:
                self.memo[robTuple] = self.moneyHeist(robTuple)

            if notRobTuple not in self.memo:
                self.memo[notRobTuple] = self.moneyHeist(notRobTuple)

            # rob
            robMoney = nums[0] + self.memo[robTuple]

            # not rob
            notRobMoney = self.memo[notRobTuple]
            
            return max(notRobMoney, robMoney)

    def rob(self, nums: List[int]) -> int:
        self.memo = {}
        return self.moneyHeist(nums)
    """

    # Bottom Up Tabulation, Time-O(n) Space-O(n)
    def rob(self, nums: List[int]) -> int:
        nums.extend([0, 0])

        n = len(nums)

        dp = [0] * n

        for index in range(n - 3, -1, -1):
            dp[index] = max(nums[index] + dp[index + 2], dp[index + 1])

        return dp[0]


print(Solution().rob([2, 1, 1, 2]))
print(Solution().rob([2, 7, 9, 3, 1]))
