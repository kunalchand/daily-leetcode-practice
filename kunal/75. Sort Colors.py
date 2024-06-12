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


# https://leetcode.com/problems/sort-colors/
class Solution:
    # In-Place Sort
    '''
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
    '''

    # Two Pointer, Time-O(n) Space-O(n)
    """
    def sortColors(self, nums: List[int]) -> None:
        left = deque()
        right = deque()

        dq = deque(nums)

        while dq:
            num = dq.popleft()
            if num == 0:
                left.appendleft(num)
            elif num == 1:
                left.append(num)
            elif num == 2:
                right.append(num)
        
        for index, num in enumerate(list(left + right)):
            nums[index] = num
    """

    # Two Pointer, Two Pass, Time-O(n) Space-O(1)
    """
    def sortColors(self, nums: List[int]) -> None:
        count = Counter(nums)

        for index in range(len(nums)):
            if count[0] > 0:
                nums[index] = 0
                count[0] -= 1
            elif count[1] > 0:
                nums[index] = 1
                count[1] -= 1
            else:
                nums[index] = 2
    """

    # Two Pointer, One Pass, Time-O(n) Space-O(1)
    # Reference (Nick White): https://www.youtube.com/watch?v=uvB-Ns_TVis
    def sortColors(self, nums: List[int]) -> None:
        start = 0
        end = len(nums) - 1

        index = 0

        while start <= end and index <= end:
            if nums[index] == 0:
                nums[start], nums[index] = nums[index], nums[start]
                start += 1
                index += 1
            elif nums[index] == 2:
                nums[index], nums[end] = nums[end], nums[index]
                end -= 1
            else:
                index += 1
