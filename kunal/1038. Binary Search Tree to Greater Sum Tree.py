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


# https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/
class Solution:
    def recursion(self, root: TreeNode) -> None:
        if not root:
            return
        else:
            self.recursion(root.right)
            root.val += self.sum
            self.sum = root.val
            self.recursion(root.left)

    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.sum = 0
        self.recursion(root)
        return root
