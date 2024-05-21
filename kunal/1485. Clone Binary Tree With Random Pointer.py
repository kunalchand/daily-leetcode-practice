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


# Definition for NodeCopy.
class NodeCopy:
    def __init__(self, val=0, left=None, right=None, random=None):
        self.val = val
        self.left = left
        self.right = right
        self.random = random


# Definition for Node.
class Node:
    def __init__(self, val=0, left=None, right=None, random=None):
        self.val = val
        self.left = left
        self.right = right
        self.random = random


# https://leetcode.com/problems/clone-binary-tree-with-random-pointer/
class Solution:
    def createHashmap(self, root) -> None:
        if not root:
            return

        self.hashmap[root] = NodeCopy(root.val)

        self.createHashmap(root.left)
        self.createHashmap(root.right)

    def generatePointer(self, node) -> None:
        if not node:
            return

        nodeCopy = self.hashmap[node]
        if node.left:
            nodeCopy.left = self.hashmap[node.left]
        if node.right:
            nodeCopy.right = self.hashmap[node.right]
        if node.random:
            nodeCopy.random = self.hashmap[node.random]

        self.generatePointer(node.left)
        self.generatePointer(node.right)

    def copyRandomBinaryTree(self, root: "Optional[Node]") -> "Optional[NodeCopy]":
        if not root:
            return root

        self.hashmap = {}

        self.createHashmap(root)

        self.generatePointer(root)

        return self.hashmap[root]
