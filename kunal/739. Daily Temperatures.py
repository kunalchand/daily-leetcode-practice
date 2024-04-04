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


# https://leetcode.com/problems/daily-temperatures/
class Solution:
    # Time-O(n) Space-O(n) Monotonic Stack (Right to Left)
    """
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)

        monotonic_stack = []

        for index in range(len(temperatures)-1, -1, -1):
            temperature = temperatures[index]
            while monotonic_stack and temperature >= monotonic_stack[-1][0]:
                monotonic_stack.pop()

            if monotonic_stack :
                ans[index] = monotonic_stack[-1][1] - index
            else:
                ans[index] = 0

            monotonic_stack.append([temperature, index])

        return ans
    """

    # Time-O(n) Space-O(n) Monotonic Stack (Left to Right)
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)

        monotonic_stack = []

        for index in range(len(temperatures)):
            temperature = temperatures[index]
            while monotonic_stack and monotonic_stack[-1][0] < temperature:
                ans[monotonic_stack[-1][1]] = index - monotonic_stack[-1][1]
                monotonic_stack.pop()

            monotonic_stack.append([temperature, index])

        return ans


print(Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
print(Solution().dailyTemperatures([30, 40, 50, 60]))
print(Solution().dailyTemperatures([30, 60, 90]))
