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


# https://leetcode.com/problems/largest-positive-integer-that-exists-with-its-negative/
class Solution:
    # Two Pointer, Time-O(n*logn) Space-O(1)
    """
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()

        left = -1
        right = len(nums)

        for index in range(len(nums)):
            if nums[index] < 0:
                left = max(left, index)
            else:
                right = min(right, index)

        ans = -1

        while 0 <= left and right < len(nums):
            if -nums[left] == nums[right]:
                ans = nums[right]
                left -= 1
                right += 1
            elif -nums[left] > nums[right]:
                right += 1
            elif -nums[left] < nums[right]:
                left -= 1

        return ans
    """

    # Hashset, Time-O(n) Space-O(n)
    def findMaxK(self, nums: List[int]) -> int:
        hashset = set(nums)

        ans = -1

        for num in nums:
            if -num in hashset:
                ans = max(ans, abs(num))

        return ans


print(Solution().findMaxK([-1, 2, -3, 3]))
print(Solution().findMaxK([-1, 10, 6, 7, -7, 1]))
print(Solution().findMaxK([-10, 8, 6, 7, -2, -3]))
