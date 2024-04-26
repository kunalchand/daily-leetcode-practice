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


# https://leetcode.com/problems/graph-valid-tree/
class Solution:
    def generateGraph(self, edges: List[List[int]], graph: Dict) -> None:
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = defaultdict(list)
        self.generateGraph(edges, graph)

        visited = set()
        queue = deque()

        visited.add(0)
        queue.append([0, -1])

        while queue:
            parent, grandparent = queue.popleft()

            for child in graph[parent]:
                if child not in visited:
                    visited.add(child)
                    queue.append([child, parent])

                elif child in visited and child != grandparent:
                    return False

        return True if len(visited) == n else False


print(Solution().validTree(5, [[0, 1], [0, 2], [0, 3], [1, 4]]))
print(Solution().validTree(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]))
