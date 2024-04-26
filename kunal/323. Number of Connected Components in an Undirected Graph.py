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


# https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/
class Solution:
    # BFS, Time-O(n) Space-O(n)
    """
    def generateGraph(self, edges: List[List[int]], graph: Dict) -> None:
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

    def BFS(self, graph: Dict, start: int) -> None:
        self.visited.add(start)
        self.queue.append(start)

        while self.queue:
            parent = self.queue.popleft()

            for child in graph[parent]:
                if child not in self.visited:
                    self.visited.add(child)
                    self.queue.append(child)

    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        self.generateGraph(edges, graph)

        self.visited = set()
        self.queue = deque()

        count = 0

        for start in range(n):
            if start not in self.visited:
                self.BFS(graph, start)
                count += 1

        return count
    """

    # DFS, Time-O(n) Space-O(n)
    def generateGraph(self, edges: List[List[int]], graph: Dict) -> None:
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

    def DFS(self, graph: Dict, start: int) -> None:
        for child in graph[start]:
            if child not in self.visited:
                self.visited.add(child)
                self.DFS(graph, child)

    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        self.generateGraph(edges, graph)

        self.visited = set()

        count = 0

        for start in range(n):
            if start not in self.visited:
                self.DFS(graph, start)
                count += 1

        return count


print(Solution().countComponents(5, [[0, 1], [1, 2], [3, 4]]))
print(Solution().countComponents(5, [[0, 1], [1, 2], [2, 3], [3, 4]]))
