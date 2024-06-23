"""
LC 977: https://leetcode.com/problems/squares-of-a-sorted-array/description/
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

 

Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].

[-a -b -c -d e f g h i k]

[ee ff gg hh ii kk] <=
 => [dd cc bb aa]

[-4,-1,-1,0,1,3,3,10]
[0, 1, 9, 9, 100]
[1, 1, 16]

[0 1 1 1 9 9 16 100]
"""

import bisect
import copy
import heapq
import math
import random
from bisect import bisect, bisect_left, bisect_right, insort, insort_left, insort_right
from collections import Counter, defaultdict, deque
from dataclasses import dataclass
from functools import cache, cmp_to_key, lru_cache, reduce
from itertools import combinations, pairwise, permutations, zip_longest
from math import ceil, factorial, floor, inf, sqrt
from typing import Deque, Dict, List, Optional, Set, Tuple, Union


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        positive_squares = deque()
        negative_squares = deque()

        # Prepare Deques
        for num in nums:
            if num < 0:  # Append on Left
                negative_squares.appendleft(num * num)
            else:  # Append on Right
                positive_squares.append(num * num)

        output = []

        # Merge
        while positive_squares and negative_squares:
            ps = positive_squares[0]
            ns = negative_squares[0]

            if ps < ns:
                output.append(ps)
                positive_squares.popleft()
            else:
                output.append(ns)
                negative_squares.popleft()

        # Append Remaining Elements
        while positive_squares:
            output.append(positive_squares.popleft())

        while negative_squares:
            output.append(negative_squares.popleft())

        return output
