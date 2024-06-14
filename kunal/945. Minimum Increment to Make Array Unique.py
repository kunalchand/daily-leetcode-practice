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


# https://leetcode.com/problems/minimum-increment-to-make-array-unique/
class Solution:
    # Brute Force TLE - 55/63
    """
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        numsCount = Counter(nums)
        moves = 0
        for index, num in enumerate(nums):
            if numsCount[num] > 1:
                numsCount[num] -= 1
                while num in numsCount:
                    num += 1
                    moves += 1
                nums[index] = num
                numsCount[num] += 1
        return moves
    """

    # Heap
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.append(float("inf"))
        nums.sort()
        numsCount = Counter(nums)
        moves = 0

        # Store possible newNums
        minHeap = []
        for index in range(1, len(nums)):
            if nums[index] - nums[index - 1] > 1:
                newNum = nums[index - 1] + 1
                lowerBound = nums[index - 1] + 1
                upperBound = nums[index] - 1
                heapq.heappush(minHeap, [newNum, lowerBound, upperBound])

        for index, num in enumerate(nums):
            if numsCount[num] > 1:
                numsCount[num] -= 1

                while minHeap[0][0] < num:
                    heapq.heappop(minHeap)

                newNum, lowerBound, upperBound = heapq.heappop(minHeap)
                nums[index] = newNum
                moves += newNum - num

                if lowerBound < upperBound:
                    heapq.heappush(
                        minHeap, [lowerBound + 1, lowerBound + 1, upperBound]
                    )

        return moves
