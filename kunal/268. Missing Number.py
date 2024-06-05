import bisect
import copy
import heapq
import math
import random
from bisect import bisect, bisect_left, bisect_right, insort, insort_left, insort_right
from collections import Counter, defaultdict, deque
from dataclasses import dataclass
from functools import cmp_to_key, reduce
from itertools import combinations, pairwise, permutations, zip_longest
from math import ceil, factorial, floor, sqrt
from typing import Dict, List, Optional, Set, Tuple, Union


# https://leetcode.com/problems/missing-number/
class Solution:
    # Set Bits, Time-O(n) Space-O(?)
    """
    def missingNumber(self, nums: List[int]) -> int:
        setBits = 0
        for num in nums:
            setBits |= 1 << num

        for n in range(0, len(nums)+1):
            if setBits & 1 == 0:
                return n
            else:
                setBits = setBits >> 1
    """

    # XOR, Time-O(n) Space-O(1)
    """
    def missingNumber(self, nums: List[int]) -> int:
        xorAll = 0

        for n in range(0, len(nums)+1):
            xorAll ^= n

        for num in nums:
            xorAll ^= num
        
        return xorAll
    """

    # Math, Time-O(n) Space-O(1)
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        totalSum = n * (n + 1) // 2
        return totalSum - sum(nums)
