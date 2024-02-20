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


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.minHeap = []
        self.k = k

        for num in nums:
            if self.minHeap:
                if len(self.minHeap) < self.k:
                    heapq.heappush(self.minHeap, num)
                elif len(self.minHeap) == self.k and num >= self.minHeap[0]:
                    heapq.heappush(self.minHeap, num)
                    heapq.heappop(self.minHeap)
            else:
                heapq.heappush(self.minHeap, num)

    def add(self, val: int) -> int:
        if self.minHeap:
            if len(self.minHeap) < self.k:
                heapq.heappush(self.minHeap, val)
            elif len(self.minHeap) == self.k and val >= self.minHeap[0]:
                heapq.heappush(self.minHeap, val)
                heapq.heappop(self.minHeap)
        else:
            heapq.heappush(self.minHeap, val)

        return self.minHeap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
