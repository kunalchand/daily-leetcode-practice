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


# https://leetcode.com/problems/sum-of-square-numbers/
class Solution:
    # Two Sum One Pass, Time-O(sqrt(c)) Space-O(sqrt(c))
    """
    def twoSum(self, nums: List[int], target: int) -> bool:
        hashset = set()

        for num in nums:
            counterPart = target - num
            if counterPart in hashset:
                return True
            hashset.add(num)

        return False

    def judgeSquareSum(self, c: int) -> bool:
        nums = []
        for num in range(floor(sqrt(c))+1):
            nums.append(num*num)
            nums.append(num*num)

        return self.twoSum(nums, c)
    """

    # Two Pointer w/ deque, Time-O(sqrt(c)) Space-O(sqrt(c))
    def judgeSquareSum(self, c: int) -> bool:
        nums = deque()
        for num in range(floor(sqrt(c)) + 1):
            nums.append(num * num)
            nums.append(num * num)

        while len(nums) > 1:
            left = nums[0]
            right = nums[-1]

            if left + right > c:
                nums.pop()
            elif left + right < c:
                nums.popleft()
            elif left + right == c:
                return True

        return False
