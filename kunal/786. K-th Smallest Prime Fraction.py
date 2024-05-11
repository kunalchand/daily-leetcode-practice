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


# https://leetcode.com/problems/k-th-smallest-prime-fraction/
class Solution:
    # MinHeap, Time-O((n+k)*logn) Space-O(n)
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        minHeap = []

        for index in range(len(arr) - 1):
            numerator = index
            denominator = len(arr) - 1
            fraction = arr[numerator] / arr[denominator]
            heapq.heappush(minHeap, [fraction, numerator, denominator])

        while True:
            fraction, numerator, denominator = heapq.heappop(minHeap)
            k -= 1
            if k == 0:
                return [arr[numerator], arr[denominator]]

            denominator = denominator - 1
            fraction = arr[numerator] / arr[denominator]

            if numerator < denominator:
                heapq.heappush(minHeap, [fraction, numerator, denominator])

    """
    Explanation of MinHeap Approach:
    If we group all the fractions with same numerator together, 
    you can see we are basically dealing with a bunch of sorted arrays. 
    For example, [1, 2, 3, 5] has these fractions:

        group 1 -> 1/5, 1/3, 1/2
        group 2 -> 2/5, 2/3
        group 3 -> 3/5

    Now the question becomes merging k sorted lists: 
    https://leetcode.com/problems/merge-k-sorted-lists/. When filling the queue initially, 
    we are inserting the smallest fraction for each group (or the head of each sorted 
    array, hence the denominator is fixed), then during each iteration, we are picking 
    the group with smallest fraction and then move to the next larger fraction in that 
    group (such as from 1/5 to 1/3, hence the numerator is fixed this time).
    """
