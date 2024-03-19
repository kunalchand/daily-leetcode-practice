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
    # Recursive (No Helper Method)
    """
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        elif len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        else:
            mid = len(nums) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                index = self.search(nums[:mid], target)
                return index if index != -1 else -1
            elif nums[mid] < target:
                index = self.search(nums[mid + 1 :], target)
                return 1 + mid + index if index != -1 else -1

            return -1
    """

    # Recursive (Helper Method)
    """
    def binarySearch(self, nums: List[int], target: int, left: int, right: int) -> int:
        if left > right:
            return -1
        elif left == right:
            if nums[left] == target:
                return left
            else:
                return -1
        else:
            mid = (right + left) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                index = self.binarySearch(nums, target, left, mid-1)
                return index
            else:
                index = self.binarySearch(nums, target, mid+1, right)
                return index
            

    def search(self, nums: List[int], target: int) -> int:
        return self.binarySearch(nums, target, 0, len(nums)-1)
    """

    # Iterative
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (right + left) // 2

            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                right = mid - 1
            elif nums[mid] < target:
                left + mid + 1

        return -1
