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
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-stone for stone in stones]
        heapq.heapify(maxHeap)

        while True:
            if len(maxHeap) == 0:
                return 0
            elif len(maxHeap) == 1:
                return -maxHeap[0]
            else:
                stone1 = -heapq.heappop(maxHeap)
                stone2 = -heapq.heappop(maxHeap)

                if abs(stone1 - stone2) != 0:
                    heapq.heappush(maxHeap, -abs(stone1 - stone2))


print(Solution().lastStoneWeight([2, 7, 4, 1, 8, 1]))
print(Solution().lastStoneWeight([1]))
