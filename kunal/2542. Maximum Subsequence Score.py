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


# https://leetcode.com/problems/maximum-subsequence-score/
class Solution:
    # Reference: https://www.youtube.com/watch?v=o8emK4ehhq0
    # Time-O(n*logn) Space-O(n + k)
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        box = list(zip(nums1, nums2))
        box.sort(key=lambda item: item[1], reverse=True)  # O(n*logn)

        minHeap = []
        maxSum = 0

        for index in range(k - 1):  # O(k*logk)
            one, two = box[index]
            heapq.heappush(minHeap, one)
            maxSum += one

        score = float("-inf")
        for index in range(k - 1, len(box)):  # O(n*logk)
            one, two = box[index]
            score = max(score, (maxSum + one) * two)

            heapq.heappush(minHeap, one)
            maxSum += one
            maxSum -= minHeap[0]
            heapq.heappop(minHeap)

        return score


print(Solution().maxScore([1, 3, 3, 2], [2, 1, 3, 4], 3))
print(Solution().maxScore([4, 2, 3, 1, 1], [7, 5, 10, 9, 6], 1))
