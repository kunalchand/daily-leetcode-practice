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


# https://leetcode.com/problems/house-robber-ii/
class Solution:
    # Recursion, Time-O(?) Space-O(1)
    """
    def heist(self, nums: List[int], index: int) -> int:
        if index >= len(nums):
            return 0
        else:
            return max(nums[index] + self.heist(nums, index+2), self.heist(nums, index+1))

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        else:
            return max(self.heist(nums[:-1], 0), self.heist(nums[1:], 0))
    """

    # Top Down Memoization, Time-O(n) Space-O(n)
    """
    def heist(self, nums: List[int], index: int) -> int:
        if index >= len(nums):
            return 0
        else:
            if index+2 not in self.memo:
                self.memo[index+2] = self.heist(nums, index+2)
            if index+1 not in self.memo:
                self.memo[index+1] = self.heist(nums, index+1)

            return max(nums[index] + self.memo[index+2], self.memo[index+1])

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        else:
            self.memo = {}
            robFirstHouse = self.heist(nums[:-1], 0)

            self.memo = {}
            notRobFirstHouse = self.heist(nums[1:], 0)

            return max(robFirstHouse, notRobFirstHouse)
    """

    # Bottom UP Tabulation, Time-O(n) Space-O(n)
    def heist(self, nums: List[int], index: int) -> int:
        nums.extend([0, 0])
        n = len(nums)
        dp = [0] * n

        for index in range(n - 3, -1, -1):
            dp[index] = max(nums[index] + dp[index + 2], dp[index + 1])

        return dp[0]

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        else:
            return max(self.heist(nums[:-1], 0), self.heist(nums[1:], 0))


print(Solution().rob([2, 3, 2]))
print(Solution().rob([1, 2, 3, 1]))
print(Solution().rob([1, 2, 3]))
