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
    # Time-O(log n)
    def linearSearch(self, nums: List[int], target: int, left: int, right: int) -> int:
        while left <= right:
            if nums[left] == target:
                return left
            left += 1

        return -1

    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while True:
            if right - left < 3:
                return self.linearSearch(nums, target, left, right)
            else:
                mid = (left + right) // 2
                # Left Half is strictly increasing
                if nums[left] < nums[mid]:
                    if nums[left] <= target <= nums[mid]:
                        right = mid
                    else:
                        left = mid
                # Right Half is strictly increasing
                elif nums[mid] < nums[right]:
                    if nums[mid] <= target <= nums[right]:
                        left = mid
                    else:
                        right = mid

        return -1
