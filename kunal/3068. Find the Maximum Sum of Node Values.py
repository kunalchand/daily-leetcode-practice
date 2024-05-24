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


# https://leetcode.com/problems/find-the-maximum-sum-of-node-values/
class Solution:
    # Greedy, Time-O(n) Space-O(n)
    # Reference (Aryan Mittal): https://www.youtube.com/watch?v=3t7y4mBJDoM
    """
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        pos = []
        neg = []

        for num in nums:
            if (num^k) > num:
                pos.append((num^k) - num)
            else:
                neg.append((num^k) - num)

        # Even nodes to operate (flip)
        if len(pos)%2 == 0:
            return sum(nums) + sum(pos)
        # Odd nodes to operate (flip)
        else:
            if len(neg) == 0:
                return sum(nums) + sum(pos) - min(pos)
            else:
                return max(
                    sum(nums) + sum(pos) - min(pos),
                    sum(nums) + sum(pos) + max(neg)
                )
    """

    # Recursion (TLE - 353/717)
    """
    def backtrack(self, index: int, operationParity: bool) -> int:
        if index >= self.n:
            if operationParity:
                return 0
            else:
                return float('-inf')

        maxSum = float('-inf')

        # Choose
        maxSum = max(maxSum, (self.nums[index]^self.k) + self.backtrack(index + 1, not operationParity))

        # Not Choose
        maxSum = max(maxSum, self.nums[index] + self.backtrack(index + 1, operationParity))
        
        return maxSum

    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        self.n = len(nums)
        self.nums = nums
        self.k = k

        return self.backtrack(0, True)
    """

    # Flawed DP (TLE - 455/717)
    """
    def backtrack(self, index: int) -> int:
        if index >= self.n:
            return 0
        
        if index in self.memo:
            return self.memo[index]

        maxSum = float('-inf')

        # Choose
        for idx in range(index + 1, self.n):
            maxSum = max(maxSum, (self.nums[index]^self.k) + (self.prefixSum[idx-1] - self.prefixSum[index]) + (self.nums[idx]^self.k) + self.backtrack(idx + 1))

        # Not Choose
        maxSum = max(maxSum, self.nums[index] + self.backtrack(index + 1))
        
        self.memo[index] = maxSum

        return maxSum

    def calculatePrefixSum(self):
        for index in range(1, self.n):
            self.prefixSum[index] = self.prefixSum[index-1] + self.nums[index]

    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        self.n = len(nums)
        self.nums = nums
        self.k = k
        self.memo = {}

        self.prefixSum = [0] * (self.n)
        self.calculatePrefixSum()

        return self.backtrack(0)
    """

    # DP, Top Down Memoization, Time-O(n) Space-O(n)
    def backtrack(self, index: int, operationParity: bool) -> int:
        if index >= self.n:
            if operationParity:
                return 0
            else:
                return float("-inf")

        if (index, operationParity) in self.memo:
            return self.memo[(index, operationParity)]

        maxSum = float("-inf")

        # Choose
        maxSum = max(
            maxSum,
            (self.nums[index] ^ self.k)
            + self.backtrack(index + 1, not operationParity),
        )

        # Not Choose
        maxSum = max(
            maxSum, self.nums[index] + self.backtrack(index + 1, operationParity)
        )

        self.memo[(index, operationParity)] = maxSum
        return maxSum

    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        self.n = len(nums)
        self.nums = nums
        self.k = k
        self.memo = {}
        return self.backtrack(0, True)


print(Solution().maximumValueSum([1, 2, 1], 3, [[0, 1], [0, 2]]))
print(Solution().maximumValueSum([2, 3], 7, [[0, 1]]))
print(
    Solution().maximumValueSum(
        [7, 7, 7, 7, 7, 7], 3, [[0, 1], [0, 2], [0, 3], [0, 4], [0, 5]]
    )
)
