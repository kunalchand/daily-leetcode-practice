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
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        # Row Selection
        row = -1

        top, bottom = 0, m - 1
        while top <= bottom:
            mid = (bottom + top) // 2
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                row = mid
                break
            elif target < matrix[mid][0]:
                bottom = mid - 1
            elif matrix[mid][-1] < target:
                top = mid + 1

        if row == -1:
            return False

        # Coloum Selection
        left, right = 0, n - 1
        while left <= right:
            mid = (right + left) // 2
            if matrix[row][mid] == target:
                return True
            elif target < matrix[row][mid]:
                right = mid - 1
            elif matrix[row][mid] < target:
                left = mid + 1

        return False
