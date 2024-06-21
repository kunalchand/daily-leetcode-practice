import bisect
import copy
import heapq
import math
import random
from bisect import bisect, bisect_left, bisect_right, insort, insort_left, insort_right
from collections import Counter, defaultdict, deque
from dataclasses import dataclass
from functools import cache, cmp_to_key, lru_cache, reduce
from itertools import combinations, pairwise, permutations, zip_longest
from math import ceil, factorial, floor, inf, sqrt
from typing import Deque, Dict, List, Optional, Set, Tuple, Union


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Brute Force
"""
    def generatePOrder(self, root: 'TreeNode', p: 'TreeNode') -> None:
        if not root: 
            return
        else:
            self.p_order.append(root)

            if root.val == p.val:
                return
            elif root.val < p.val:
                self.generatePOrder(root.right, p)
            elif root.val > p.val:
                self.generatePOrder(root.left, p)
    
    def generateQOrder(self, root: 'TreeNode', q: 'TreeNode') -> bool:
        if not root: 
            return False
        else:
            self.q_order.append(root)

            if root.val == q.val:
                return True
                
            foundInLeft = self.generateQOrder(root.left, q)
            foundInRight = self.generateQOrder(root.right, q)

            if foundInLeft or foundInRight:
                return True
            else:
                self.q_order.pop()
                return False

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.p_order = []
        self.q_order = []

        self.generatePOrder(root, p)
        self.generateQOrder(root, q)

        lca = None

        for p_node, q_node in zip(self.p_order, self.q_order):
            if p_node.val == q_node.val:
                lca = p_node
            else:
                break
        
        return lca
"""


# Recursin w/ lots of conditions
"""
class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        if root.val == p.val:
            return p
        elif root.val == q.val:
            return q
        elif (p.val < root.val and q.val > root.val) or (
            q.val < root.val and p.val > root.val
        ):
            return root
        elif p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
"""


# Recursion (simplified)
class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        if root.val == p.val or root.val == q.val:
            return root
        else:
            if p.val < root.val and q.val < root.val:
                return self.lowestCommonAncestor(root.left, p, q)
            elif p.val > root.val and q.val > root.val:
                return self.lowestCommonAncestor(root.right, p, q)
            else:
                return root
