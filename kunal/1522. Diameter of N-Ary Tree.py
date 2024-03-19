import copy
import heapq
import math
import random
from collections import Counter, defaultdict, deque
from dataclasses import dataclass
from functools import cmp_to_key, reduce
from itertools import zip_longest
from math import factorial, sqrt
from typing import Dict, List, Optional, Set, Tuple, Union


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []


class Solution:
    def diameter(self, root: "Node") -> int:
        """
        :type root: 'Node'
        :rtype: int
        """
        diameter = 0

        def dfs(root: "Node") -> int:
            nonlocal diameter

            if not root:
                return 0

            depth = []

            # Calculate depth
            for child in root.children:
                depth.append(dfs(child))

            # Assign Diameter
            firstMax, secondMax = 0, 0
            firstMaxIndex = -1

            for d in depth:
                firstMax = max(firstMax, d)
                firstMaxIndex = depth.index(firstMax)

            for index, d in enumerate(depth):
                if index != firstMaxIndex:
                    secondMax = max(secondMax, d)

            diameter = max(diameter, firstMax + secondMax)

            # Return Depth
            return 1 + max([0] + depth)

        dfs(root)
        return diameter
