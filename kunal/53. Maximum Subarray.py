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
from typing import Deque, Dict, List, Optional, Set, Tuple, Union


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
    """
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
    """

    # Sliding Window, Time-O(n) Space-(1)
    class Solution:
        def maxSubArray(self, nums: List[int]) -> int:
            left = 0
            # right = 0
            windowSum = 0
            maxSum = -inf

            for num in nums:

                while windowSum < 0:
                    windowSum -= nums[left]
                    left += 1

                windowSum += num
                # right += 1
                maxSum = max(maxSum, windowSum)

            return maxSum


print(Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(Solution().maxSubArray([1]))
print(Solution().maxSubArray([5, 4, -1, 7, 8]))
