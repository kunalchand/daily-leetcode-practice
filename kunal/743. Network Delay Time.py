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


# https://leetcode.com/problems/network-delay-time/
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)

        # Generate Graph
        for time in times:
            u, v, w = time
            graph[u].append((v, w))

        visited = set()
        minHeap = []

        minTime = float("-inf")

        # Start Signal From k node
        heapq.heappush(minHeap, (0, k))

        while minHeap:
            time, node = heapq.heappop(minHeap)

            if node in visited:
                continue
            else:
                minTime = max(minTime, time)
                visited.add(node)

                # Add nearest potential neighbours
                for neighbour, w in graph[node]:
                    if neighbour not in visited:
                        heapq.heappush(minHeap, (time + w, neighbour))

        return minTime if len(visited) == n else -1
