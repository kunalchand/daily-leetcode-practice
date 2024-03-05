import copy
import heapq
import math
import random
from collections import Counter, defaultdict, deque
from dataclasses import dataclass
from functools import cmp_to_key, reduce
from itertools import zip_longest
from math import factorial, sqrt
from typing import Dict, List, Optional, Tuple, Union


class Solution:
    # Time-O(n*logn) Space-O(1)
    """
    def binarySearch(self, find, nums: List[int], left, right) -> int:
        if left > right:
            return -1
        else:
            mid = (right + left)//2
            if find == nums[mid]:
                return mid
            elif find < nums[mid]:
                return self.binarySearch(find, nums, left, mid - 1)
            elif find > nums[mid]:
                return self.binarySearch(find, nums, mid + 1, right)

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        size = len(numbers)
        for index, number in enumerate(numbers):
            target_index = self.binarySearch(target - number, numbers, index+1, size-1)
            if target_index != -1:
                return [index + 1, target_index + 1]
    """

    # Time-O(n) Space-O(1)
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while True:
            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]
            elif numbers[left] + numbers[right] < target:
                left += 1
            elif numbers[left] + numbers[right] > target:
                right -= 1


print(Solution().twoSum([2, 7, 11, 15], 9))
print(Solution().twoSum([2, 3, 4], 6))
print(Solution().twoSum([-1, 0], -1))
