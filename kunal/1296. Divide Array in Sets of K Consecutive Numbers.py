import bisect
import copy
import heapq
import math
import random
from bisect import bisect, bisect_left, bisect_right, insort, insort_left, insort_right
from collections import Counter, defaultdict, deque
from dataclasses import dataclass
from functools import cmp_to_key, reduce
from itertools import combinations, pairwise, permutations, zip_longest
from math import ceil, factorial, floor, sqrt
from typing import Dict, List, Optional, Set, Tuple, Union


# https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/
class Solution:
    # Heap (TLE)
    """
    def isPossibleDivide(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize != 0:
            return False
        else:
            minHeap = hand[:]
            heapq.heapify(minHeap)

            while minHeap:
                group = []
                group.append(heapq.heappop(minHeap))

                bag = []
                while len(group) < groupSize:
                    if not minHeap:
                        return False
                    elif group[-1] == minHeap[0]:
                        bag.append(heapq.heappop(minHeap))
                    elif group[-1] + 1 == minHeap[0]:
                        group.append(heapq.heappop(minHeap))
                    elif group[-1] + 1 < minHeap[0]:
                        return False

                minHeap += bag
                heapq.heapify(minHeap)

            return True
    """

    # Heap and Map
    def isPossibleDivide(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        else:
            minHeap = list(Counter(hand).items())
            heapq.heapify(minHeap)

            while minHeap:
                group = []
                bag = []

                card, freq = heapq.heappop(minHeap)
                if freq > 1:
                    bag.append((card, freq - 1))
                group.append(card)

                while len(group) < groupSize:
                    if not minHeap:
                        return False
                    elif group[-1] + 1 == minHeap[0][0]:
                        card, freq = heapq.heappop(minHeap)
                        if freq > 1:
                            bag.append((card, freq - 1))
                        group.append(card)
                    elif group[-1] + 1 < minHeap[0][0]:
                        return False

                minHeap += bag
                heapq.heapify(minHeap)

            return True
