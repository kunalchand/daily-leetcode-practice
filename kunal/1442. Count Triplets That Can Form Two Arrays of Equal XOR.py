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


# https://leetcode.com/problems/count-triplets-that-can-form-two-arrays-of-equal-xor/
class Solution:
    # Brute Force (TLE)
    """
    def countTriplets(self, arr: List[int]) -> int:
        count = 0
        for i in range(len(arr)-1):
            for j in range(i+1, len(arr)):
                for k in range(j, len(arr)):
                    a = arr[i]
                    for index in range(i+1, j):
                        a ^= arr[index]
                    b = arr[j]
                    for index in range(j+1, k+1):
                        b ^= arr[index]
                    if a == b:
                        count += 1
        return count
    """

    # XOR Property, Time-O(n*n) Space-O(n)
    def countTriplets(self, arr: List[int]) -> int:
        count = 0

        for i in range(len(arr) - 1):
            for k in range(i + 1, len(arr)):
                dq = deque()
                xor = 0

                for index in range(i, k + 1):
                    dq.append(arr[index])
                    xor ^= arr[index]

                a = 0
                b = xor

                while len(dq) > 1:
                    element = dq.popleft()

                    a ^= element
                    b ^= element

                    if a == b:
                        # print(i, k - len(dq) + 1, k)
                        count += 1

        return count
