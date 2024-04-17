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


# https://leetcode.com/problems/number-of-visible-people-in-a-queue/description/
class Solution:
    # Monotonic Stack Right To Left, Time-O(n) Space-O(n)
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        ans = [0] * len(heights)

        stack = [heights[-1]]

        for index in range(len(heights) - 2, -1, -1):
            # Can only see the next person
            if heights[index] < stack[-1]:
                ans[index] += 1
                stack.append(heights[index])

            # Can see all the people till I see a taller person
            elif heights[index] > stack[-1]:
                while stack and heights[index] > stack[-1]:
                    ans[index] += 1
                    stack.pop()

                # Can see the taller person too
                if stack:
                    ans[index] += 1

                stack.append(heights[index])

        return ans


print(Solution().canSeePersonsCount([10, 6, 8, 5, 11, 9]))
print(Solution().canSeePersonsCount([5, 1, 2, 3, 10]))
