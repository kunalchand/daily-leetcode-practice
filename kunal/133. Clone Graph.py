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


# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from typing import Optional


class Solution:
    # DFS Recursive, Time-O(n+E) Space-O(n) n-number of nodes, E-Edges
    """
    def getNode(self, value: int) -> 'Node':
        if value in self.hashmap:
            return self.hashmap[value]
        else:
            newNode = Node(value, [])
            self.hashmap[value] = newNode
            return newNode

    def deepCopyGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node or node.val in self.visited:
            return
        else:
            copyNode = self.getNode(node.val)
            self.visited.add(node.val)

            for neighbor in node.neighbors:
                copyNode.neighbors.append(self.getNode(neighbor.val))
                self.deepCopyGraph(neighbor)

            return copyNode

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node
        else:
            self.hashmap = {}
            self.visited = set()

            return self.deepCopyGraph(node)
    """

    # BFS Iterative, Time-O(n+E) Space-O(n) n-number of nodes, E-Edges
    def getNode(self, value: int) -> "Node":
        if value in self.hashmap:
            return self.hashmap[value]
        else:
            newNode = Node(value, [])
            self.hashmap[value] = newNode
            return newNode

    def deepCopyGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        copyNode = self.getNode(node.val)
        self.queue.append(node)
        self.visited.add(node.val)

        while self.queue:
            originalNode = self.queue.popleft()

            for neighbor in originalNode.neighbors:
                self.getNode(originalNode.val).neighbors.append(
                    self.getNode(neighbor.val)
                )
                if neighbor.val not in self.visited:
                    self.queue.append(neighbor)
                    self.visited.add(neighbor.val)

        return copyNode

    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if not node:
            return node
        else:
            self.hashmap = {}
            self.visited = set()
            self.queue = deque()

            return self.deepCopyGraph(node)
