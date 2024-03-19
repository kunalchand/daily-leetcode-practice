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
    # # O(log n) Recursion
    """
    def findMin(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return min(nums)
        elif nums[0] < nums[-1]:
            return nums[0]
        else:
            mid = (len(nums) - 1)//2

            if nums[0] > nums[mid]:
                return self.findMin(nums[:mid+1])
            elif nums[mid] > nums[-1]:
                return self.findMin(nums[mid:])

        return -5001
    """

    # O(log n) Iterative
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while True:
            if right - left < 3:
                return min(nums)
            elif nums[left] < nums[right]:
                return nums[0]
            else:
                mid = (left + right) // 2

                if nums[left] > nums[mid]:
                    right = mid
                elif nums[mid] > nums[right]:
                    left = mid

        return -5001
