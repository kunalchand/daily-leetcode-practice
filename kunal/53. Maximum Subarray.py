import copy
import heapq
import math
import random
from collections import Counter, defaultdict, deque
from dataclasses import dataclass
from functools import cmp_to_key, reduce
from itertools import zip_longest
from math import factorial, sqrt
from typing import Dict, List, Optional, Set, Tuple, Union


class Solution:
    # O(n*n) Brute Force
    """
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = 0
        max_sum = float('-inf')

        for i in range(len(nums)):
            for j in range(i, len(nums)):
                current_sum += nums[j]
                max_sum = max(max_sum, current_sum)

            current_sum = 0

        return max_sum
    """

    # O(n) Kadane Algorithm
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = 0
        max_sum = float("-inf")

        pointer = 0
        while pointer < len(nums):
            current_sum += nums[pointer]
            max_sum = max(max_sum, current_sum)

            if current_sum < 0:
                current_sum = 0

            pointer += 1

        return max_sum


print(Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(Solution().maxSubArray([1]))
print(Solution().maxSubArray([5, 4, -1, 7, 8]))
