import copy
import heapq
import math
import random
from collections import Counter, defaultdict, deque
from dataclasses import dataclass
from functools import cmp_to_key, reduce
from itertools import zip_longest
from math import factorial, sqrt
from typing import Dict, List, Optional, Tuple, Union


class Solution:
    # O(n*logk)
    """
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = []

        for num in nums:
            if len(minHeap) < k:
                heapq.heappush(minHeap, num)
            elif len(minHeap) == k and num >= minHeap[0]:
                heapq.heappush(minHeap, num)
                heapq.heappop(minHeap)

        return minHeap[0]
    """

    # O(n + k*logn)
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-num for num in nums]
        heapq.heapify(nums)  # O(n)

        while k > 1:
            heapq.heappop(nums)
            k -= 1

        return -nums[0]
