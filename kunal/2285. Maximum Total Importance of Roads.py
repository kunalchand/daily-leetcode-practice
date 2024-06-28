import bisect
import copy
import heapq
import math
import random
from bisect import bisect, bisect_left, bisect_right, insort, insort_left, insort_right
from collections import Counter, defaultdict, deque
from copy import deepcopy
from dataclasses import dataclass
from functools import cache, cmp_to_key, lru_cache, reduce
from heapq import heapify, heappop, heappush, heappushpop
from itertools import combinations, pairwise, permutations, zip_longest
from math import ceil, factorial, floor, inf, sqrt
from typing import Deque, Dict, List, Optional, Set, Tuple, Union


# https://leetcode.com/problems/maximum-total-importance-of-roads/
class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        graph = {}
        for a, b in roads:
            if a not in graph:
                graph[a] = []
            graph[a].append(b)
            if b not in graph:
                graph[b] = []
            graph[b].append(a)

        for city in range(0, n):
            if city not in graph:
                graph[city] = []

        maxHeap = []
        for a in graph:
            heappush(maxHeap, [-len(graph[a]), a])

        value = [0] * (n)
        for v in range(n, 0, -1):
            _, city = heappop(maxHeap)
            value[city] = v

        importance = 0
        for a, b in roads:
            importance += value[a]
            importance += value[b]

        return importance
