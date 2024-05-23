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


# https://leetcode.com/problems/delete-nodes-and-return-forest/
class Solution:
    def mark(self, root: Optional[TreeNode]) -> None:
        if not root:
            return

        if root.val in self.to_delete:
            root.val *= -1

        self.mark(root.left)
        self.mark(root.right)

    def delete(self, root: Optional[TreeNode]) -> None:
        if not root:
            return

        self.delete(root.left)
        # Remove connection to left child if the child was negative
        if root.left and root.left.val < 0:
            root.left = None

        self.delete(root.right)
        # Remove connection to right child if the child was negative
        if root.right and root.right.val < 0:
            root.right = None

        # Delete current node and add children in forest if they exists
        if root.val <= 0:
            if root.left:
                self.forest.append(root.left)
                root.left = None
            if root.right:
                self.forest.append(root.right)
                root.right = None

    def delNodes(
        self, root: Optional[TreeNode], to_delete: List[int]
    ) -> List[TreeNode]:
        self.to_delete = set(to_delete + [0])
        self.mark(root)

        self.forest = []
        self.delete(TreeNode(0, root))

        return self.forest
