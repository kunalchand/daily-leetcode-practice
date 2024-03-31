import copy
import heapq
import math
import random
from collections import Counter, defaultdict, deque
from dataclasses import dataclass
from functools import cmp_to_key, reduce
from itertools import zip_longest
from math import factorial, sqrt
from typing import Dict, List, Optional, Set, Tuple, Union


class Solution:
    # Brute Force O(n + n*logn + k)
    """
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_ = defaultdict(int)
        for num in nums:
            dict_[num] += 1
        list_ = sorted(dict_.items(), key=lambda x: -x[1])
        return [tuple_[0] for tuple_ in list_[:k]]
    """

    # Min Heap Approach O(n + k*logn)
    """
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_ = defaultdict(int)
        for num in nums:
            dict_[num] += 1
        maxHeap = [[-value,key] for key, value in dict_.items()]
        heapq.heapify(maxHeap)
        ans = []
        while k > 0:
            top = heapq.heappop(maxHeap)
            ans.append(top[1])
            k -= 1
        return ans
    """

    # Max Heap Approach O(n + n*logk)
    """
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_ = defaultdict(int)
        for num in nums:
            dict_[num] += 1
        minHeap = []
        for key, value in dict_.items():
            if len(minHeap) < k:
                heapq.heappush(minHeap, [value, key])
            else:
                top = minHeap[0]
                if top[0] < value:
                    heapq.heappush(minHeap, [value, key])
                    heapq.heappop(minHeap)
        return [list_[1] for list_ in minHeap]
    """

    # Bucket Sort Approach Time-O(n) Space-O(n)
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_ = defaultdict(int)
        for num in nums:
            dict_[num] += 1

        bucket_list = [[] for _ in nums]

        for key, value in dict_.items():
            bucket_list[value - 1].append(key)

        ans = []
        for bucket in reversed(bucket_list):
            ans.extend(bucket)
            if len(ans) == k:
                break

        return ans


print(Solution().topKFrequent([1, 1, 1, 2, 2, 3], 2))
print(Solution().topKFrequent([1], 1))
