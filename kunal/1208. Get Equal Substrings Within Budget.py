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


# https://leetcode.com/problems/get-equal-substrings-within-budget/
class Solution:
    # Two Pointer Sliding Window
    """
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        array = [0] * len(s)

        for index in range(len(s)):
            array[index] = abs(ord(s[index]) - ord(t[index]))

        maxLength = 0

        left = 0
        right = 0

        windowSum = 0

        while right < len(s):
            # Extend Window from right
            while right < len(s) and windowSum <= maxCost:
                windowSum += array[right]
                if windowSum <= maxCost:
                    maxLength = max(maxLength, right - left + 1)
                right += 1

            # Shrink Window from left
            while left <= right and windowSum > maxCost:
                windowSum -= array[left]
                left += 1

        return maxLength
    """

    # Deque Sliding Window
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        cost = deque(abs(ord(sChar) - ord(tChar)) for sChar, tChar in zip(s, t))
        window = deque()

        maxLength = 0
        windowSum = 0

        while cost:
            # Extend Window
            while cost and windowSum <= maxCost:
                windowSum += cost[0]
                window.append(cost.popleft())
                if windowSum <= maxCost:
                    maxLength = max(maxLength, len(window))

            # Shrink Window
            while window and windowSum > maxCost:
                windowSum -= window[0]
                window.popleft()

        return maxLength
