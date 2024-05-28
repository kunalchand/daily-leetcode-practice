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


# https://leetcode.com/problems/target-sum/
class Solution:
    # Recursion (TLE - 93/140)
    """
    def recursion(self, nums: List[int], target: int, index: int) -> int:
        if index >= len(nums):
            if target == 0:
                return 1
            else:
                return 0
        else:
            # +
            plusCount = self.recursion(nums, target + nums[index], index + 1)

            # -
            minusCount = self.recursion(nums, target - nums[index], index + 1)

            return plusCount + minusCount

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        return self.recursion(nums, target, 0)
    """

    # DP, Top Down Memoization Time-O(n*target) Space-O(n*target)
    def recursion(self, nums: List[int], target: int, index: int) -> int:
        if (target, index) in self.memo:
            return self.memo[(target, index)]

        if index >= len(nums):
            if target == 0:
                return 1
            else:
                return 0
        else:
            # +
            plusCount = self.recursion(nums, target + nums[index], index + 1)

            # -
            minusCount = self.recursion(nums, target - nums[index], index + 1)

            self.memo[(target, index)] = plusCount + minusCount

            return self.memo[(target, index)]

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.memo = {}
        return self.recursion(nums, target, 0)
