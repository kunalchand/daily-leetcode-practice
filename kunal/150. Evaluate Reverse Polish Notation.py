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


# https://leetcode.com/problems/evaluate-reverse-polish-notation/
class Solution:
    # Time-O(n) Space-O(n)
    def performOperation(self, first: int, second: int, operand: str) -> int:
        if operand == "+":
            return first + second
        elif operand == "-":
            return first - second
        elif operand == "*":
            return first * second
        elif operand == "/":
            if first / second >= 0:
                return math.floor(first / second)
            elif first / second < 0:
                return math.ceil(first / second)

    def evalRPN(self, tokens: List[str]) -> int:
        operands = set(["+", "-", "*", "/"])
        stack = []

        for token in tokens:
            if token not in operands:
                stack.append(int(token))
            else:
                second = stack.pop()
                first = stack.pop()

                stack.append(self.performOperation(first, second, token))

        return stack[0]


print(Solution().evalRPN(["2", "1", "+", "3", "*"]))

print(Solution().evalRPN(["4", "13", "5", "/", "+"]))

print(
    Solution().evalRPN(
        ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    )
)
