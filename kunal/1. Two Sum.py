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
    # Brute Force Time-O(n*n) Space-O(1)
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
    """

    # HashMap Two Pass Time-O(n) Space-O(n)
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for index, num in enumerate(nums):
            hashmap[num] = index
        
        for index, num in enumerate(nums):
            if target-num in hashmap and index != hashmap[target-num]:
                return [index, hashmap[target-num]]
    """

    # HashMap One Pass Time-O(n) Space-O(n)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for index, num in enumerate(nums):
            if target - num in hashmap:
                return [index, hashmap[target - num]]
            else:
                hashmap[num] = index


print(Solution().twoSum([2, 7, 11, 15], 9))
print(Solution().twoSum([3, 2, 4], 6))
print(Solution().twoSum([3, 3], 6))
