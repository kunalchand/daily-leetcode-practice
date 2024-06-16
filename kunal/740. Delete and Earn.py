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
    @cache
    def recursion(self, index: int, oldElement: int) -> int:
        if index >= len(self.nums):
            return 0
        else:
            maxPoints = 0

            # Earn
            if not self.nums[index] == oldElement + 1:
                maxPoints = max(
                    maxPoints,
                    self.nums[index] + self.recursion(index + 1, self.nums[index]),
                )

            # No Earn
            maxPoints = max(
                maxPoints,
                self.recursion(index + 1, max(oldElement, self.nums[index] - 2)),
            )

            return maxPoints

    def deleteAndEarn(self, nums: List[int]) -> int:
        self.nums = sorted(nums)
        return self.recursion(0, -inf)
