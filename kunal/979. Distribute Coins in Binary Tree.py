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


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# https://leetcode.com/problems/distribute-coins-in-binary-tree/
class Solution:
    def coinExchange(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        leftSupply = self.coinExchange(root.left)
        rightSupply = self.coinExchange(root.right)

        self.moves += abs(leftSupply) + abs(rightSupply)

        return (root.val + leftSupply + rightSupply) - 1

    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.moves = 0
        self.coinExchange(root)
        return self.moves
