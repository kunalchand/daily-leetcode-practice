import bisect
import copy
import heapq
import math
import random
from bisect import bisect, bisect_left, bisect_right, insort, insort_left, insort_right
from collections import Counter, defaultdict, deque
from dataclasses import dataclass
from functools import cmp_to_key, reduce
from itertools import zip_longest
from math import ceil, factorial, floor, sqrt
from typing import Dict, List, Optional, Set, Tuple, Union


# https://leetcode.com/problems/find-the-number-of-subarrays-where-boundary-elements-are-maximum/
class Solution:
    # Monotonic Stack + Binary Search, Time-O(n*logn) Space-O(n) [ACCEPTED]
    """
    # Reference: https://www.youtube.com/watch?v=TgyS-xFmYJc
    def generateNextGreater(self, nums: List[int]) -> int:
        stack = [(1000000001, len(nums))]

        for index in range(len(nums)-1, -1, -1):
            while nums[index] >= stack[-1][0]:
                stack.pop()

            self.nextGreater[index] = stack[-1][1]
            stack.append((nums[index], index))

    def generateDuplicates(self, nums: List[int]) -> int:
        for index, num in enumerate(nums):
            self.duplicates[num].append(index)

    def binarySearch(self, duplicate: List, left: int, right: int, find: int) -> int:
        while left <= right:
            mid = (left + right)//2

            if duplicate[mid] == find:
                return mid
            elif duplicate[mid] > find:
                right = mid - 1
            else:
                left = mid + 1

        return right

    def numberOfSubarrays(self, nums: List[int]) -> int:
        self.nextGreater = [-1] * len(nums)
        self.generateNextGreater(nums)

        self.duplicates = defaultdict(list)
        self.generateDuplicates(nums)

        count = 0

        for index, num in enumerate(nums):
            start = self.binarySearch(self.duplicates[num], 0, len(self.duplicates[num])-1, index)
            end = self.binarySearch(self.duplicates[num], 0, len(self.duplicates[num])-1, self.nextGreater[index])

            length = end - start + 1

            count += length

        return count
    """

    # Only Monotonic Stack, Time-O(n) Space-O(n)
    def countAndPop(self, stack: List) -> int:
        topNum = stack[-1]
        length = 0

        while stack and stack[-1] == topNum:
            length += 1
            stack.pop()

        # Eg. [7 7 7 7] => 4 + 3 + 2 + 1 = 4*(4+1)//2 = 10 subarrays
        return length * (length + 1) // 2

    def numberOfSubarrays(self, nums: List[int]) -> int:
        count = 0

        stack = []

        nums.append(1000000001)

        for num in nums:
            # Pop all the same elements and count all the possible subarrays
            while stack and stack[-1] < num:
                count += self.countAndPop(stack)

            # Append num making the monotonic stack non-increasing
            stack.append(num)

        return count


print(Solution().numberOfSubarrays([1, 4, 3, 3, 2]))
print(Solution().numberOfSubarrays([3, 3, 3]))
print(Solution().numberOfSubarrays([1]))
