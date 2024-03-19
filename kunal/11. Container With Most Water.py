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
    def maxArea(self, height: List[int]) -> int:
        start = 0
        end = len(height) - 1

        max_area = 0

        while start < end:
            width = end - start
            length = min(height[start], height[end])
            max_area = max(max_area, width * length)

            if height[start] == height[end]:
                start += 1
            elif height[start] < height[end]:
                start += 1
            elif height[start] > height[end]:
                end -= 1

        return max_area
