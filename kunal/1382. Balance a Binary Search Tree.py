import bisect
import copy
import heapq
import math
import random
from bisect import bisect, bisect_left, bisect_right, insort, insort_left, insort_right
from collections import Counter, defaultdict, deque
from dataclasses import dataclass
from functools import cache, cmp_to_key, lru_cache, reduce
from heapq import heapify, heappop, heappush, heappushpop
from itertools import combinations, pairwise, permutations, zip_longest
from math import ceil, factorial, floor, inf, sqrt
from typing import Deque, Dict, List, Optional, Set, Tuple, Union


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# https://leetcode.com/problems/balance-a-binary-search-tree/
class Solution:
    def inOrderTraversal(self, root: TreeNode, inOrder: List) -> None:
        if root is None:
            return
        else:
            self.inOrderTraversal(root.left, inOrder)
            inOrder.append(root.val)
            self.inOrderTraversal(root.right, inOrder)

    def generateBST(self, inOrder: List) -> TreeNode:
        if inOrder == []:
            return None
        else:
            mid = len(inOrder) // 2
            root = TreeNode(
                inOrder[mid],
                self.generateBST(inOrder[:mid]),
                self.generateBST(inOrder[mid + 1 :]),
            )
            return root

    def balanceBST(self, root: TreeNode) -> TreeNode:
        inOrder = []
        self.inOrderTraversal(root, inOrder)
        return self.generateBST(inOrder)
