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


# https://leetcode.com/problems/generate-parentheses/
class Solution:
    # Backtracking Approach
    def generate(
        self, n: int, open_count: int, close_count: int, combination: str
    ) -> None:
        if open_count < close_count or open_count > n or close_count > n:
            return
        elif open_count == close_count and open_count == n and close_count == n:
            self.ans.append(combination)
        elif open_count >= close_count:
            self.generate(n, open_count + 1, close_count, combination + "(")
            self.generate(n, open_count, close_count + 1, combination + ")")

    def generateParenthesis(self, n: int) -> List[str]:
        self.ans = []

        self.generate(n, 0, 0, "")

        return self.ans


print(Solution().generateParenthesis(3))
print(Solution().generateParenthesis(1))
print(Solution().generateParenthesis(4))
