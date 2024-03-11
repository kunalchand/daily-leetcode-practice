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


class Solution:
    # Time-O(n) Space-O(n)
    """
    def trap(self, height: List[int]) -> int:
        height.insert(0,0)
        height.append(0)

        leftMax, rightMax = [0] * len(height), [0] * len(height)

        # Fill Left Max
        for index in range(1, len(height)-1):
            leftMax[index] = max(leftMax[index-1], height[index])

        # Fill Right Max
        for index in range(len(height)-2, 0, -1):
            rightMax[index] = max(rightMax[index+1], height[index])

        water = 0
        for index in range(len(height)):
            water += max(0, min(leftMax[index], rightMax[index]) - height[index])

        return water
    """

    # Time-O(n) Space-O(1)
    def trap(self, height: List[int]) -> int:
        height.insert(0, 0)
        height.append(0)

        leftLimit, rightLimit = 0, 0
        left, right = 1, len(height) - 2

        water = 0

        while left <= right:
            if leftLimit < rightLimit:
                water += max(0, leftLimit - height[left])
                leftLimit = max(leftLimit, height[left])
                left += 1
            elif leftLimit >= rightLimit:
                water += max(0, rightLimit - height[right])
                rightLimit = max(rightLimit, height[right])
                right -= 1

        return water
