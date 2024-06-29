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


# https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/
class Solution:
    """
    def DFS(self, graph: Dict, node: int, ancestor: List) -> None:
        for child in graph[node]:
            ancestor[child].add(node)
            for a in ancestor[node]:
                ancestor[child].add(a)
            self.DFS(graph, child, ancestor)

    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)

        allNodes = set([node for node in range(n)])
        nonZeroIndegreeNodes = set()

        for source, destination in edges:
            graph[source].append(destination)
            nonZeroIndegreeNodes.add(destination)

        zeroIndegreeNodes = set()
        for node in allNodes:
            if node not in nonZeroIndegreeNodes:
                zeroIndegreeNodes.add(node)

        ancestor = [set() for _ in range(n)]

        # BFS (WA - Doesn't update ancestor in order)
        # visited = set()
        # queue = deque()

        # for node in zeroIndegreeNodes:
        #     visited.add(node)
        #     queue.append(node)

        # while queue:
        #     node = queue.popleft()

        #     for child in graph[node]:
        #         ancestor[child] += [node] + ancestor[node]
        #         if child not in visited:
        #             visited.add(child)
        #             queue.append(child)

        # DFS (TLE)
        for node in zeroIndegreeNodes:
            self.DFS(graph, node, ancestor)

        for index in range(len(ancestor)):
            ancestor[index] = sorted(ancestor[index])

        return ancestor
    """

    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        pass
