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


# https://leetcode.com/problems/faulty-keyboard/
class Solution:
    # Brute Force
    """
    def finalString(self, s: str) -> str:
        ans = ""
        for char in s:
            if char == "i":
                ans = "".join(reversed(ans))
            else:
                ans += char
        return ans
    """

    # Deque, Without Multiple Reversal, Time-O(n) Space-O(n)
    # Reference: https://leetcode.com/problems/faulty-keyboard/solutions/3871597/o-n-solution-without-reversing-each-time
    def finalString(self, s: str) -> str:
        reverseCount = 0
        dq = deque()
        addDirection = "right"

        for char in s:
            if char == "i":
                reverseCount += 1
                if addDirection == "right":
                    addDirection = "left"
                elif addDirection == "left":
                    addDirection = "right"
            else:
                if addDirection == "right":
                    dq.append(char)
                elif addDirection == "left":
                    dq.appendleft(char)

        ans = ""

        while dq:
            ans += dq.popleft()

        if reverseCount % 2 == 0:
            return ans
        else:
            return "".join(reversed(ans))
