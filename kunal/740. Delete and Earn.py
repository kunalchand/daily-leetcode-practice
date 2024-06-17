import bisect
import copy
import heapq
import math
import random
from bisect import bisect, bisect_left, bisect_right, insort, insort_left, insort_right
from collections import Counter, defaultdict, deque
from dataclasses import dataclass
from functools import cache, cmp_to_key, lru_cache, reduce
from itertools import combinations, pairwise, permutations, zip_longest
from math import ceil, factorial, floor, inf, sqrt
from typing import Dict, List, Optional, Set, Tuple, Union


# https://leetcode.com/problems/delete-and-earn/
# Similar to 3186. Maximum Total Damage With Spell Casting - https://leetcode.com/problems/maximum-total-damage-with-spell-casting/
class Solution:
    # 2D DP Top Down Memoization
    """
    @cache
    def recursion(self, index: int, oldElement: int) -> int:
        if index >= len(self.nums):
            return 0
        else:
            maxPoints = 0

            # Earn
            if not self.nums[index] == oldElement + 1:
                maxPoints = max(maxPoints, self.nums[index] + self.recursion(index+1, self.nums[index]))

            # No Earn
            maxPoints = max(maxPoints, self.recursion(index+1, max(oldElement, self.nums[index] - 2)))

            return maxPoints

    def deleteAndEarn(self, nums: List[int]) -> int:
        self.nums = sorted(nums)
        return self.recursion(0, -inf)
    """

    # 1D DP Top Down Memoization
    @cache
    def recursion(self, index: int) -> int:
        if index >= len(self.nums):
            return 0
        else:
            # Earn
            num, freq = self.nums[index]
            earnPoints = num * freq
            if index + 1 < len(self.nums) and self.nums[index + 1][0] != num + 1:
                earnPoints += self.recursion(index + 1)
            else:
                earnPoints += self.recursion(index + 2)

            # No Earn
            notEarnPoints = self.recursion(index + 1)

            return max(earnPoints, notEarnPoints)

    def deleteAndEarn(self, nums: List[int]) -> int:
        self.nums = sorted(Counter(nums).items())
        return self.recursion(0)
