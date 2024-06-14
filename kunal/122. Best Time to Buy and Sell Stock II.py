import bisect
import copy
import heapq
import math
import random
from bisect import bisect, bisect_left, bisect_right, insort, insort_left, insort_right
from collections import Counter, defaultdict, deque
from dataclasses import dataclass
from functools import cmp_to_key, reduce
from itertools import combinations, pairwise, permutations, zip_longest
from math import ceil, factorial, floor, sqrt
from typing import Dict, List, Optional, Set, Tuple, Union


# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
class Solution:
    # Sliding Window, w/ deque Time-O(n) Space-O(n)
    # Reference: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/editorial/
    def maxProfit(self, prices: List[int]) -> int:
        prices = deque(prices)
        window = deque()

        profit = 0

        while prices:
            if not window:
                window.append(prices.popleft())
            else:
                if window[-1] <= prices[0]:
                    window.append(prices.popleft())
                else:
                    profit += window[-1] - window[0]
                    window.clear()

        profit += window[-1] - window[0]

        return profit

    # Sliding Window, w/ pointer Time-O(n) Space-O(1)
    # Reference: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/editorial/
    """
    def maxProfit(self, prices: List[int]) -> int:
        left, right = -1, -1
        current = 0

        profit = 0

        while current < len(prices):
            if left == -1 and right == -1:
                left, right = current, current
            else:
                if prices[right] <= prices[current]:
                    right += 1
                else:
                    profit += prices[right] - prices[left]
                    left, right = -1, -1
                    current -= 1
            current += 1
                
        profit += prices[right] - prices[left]

        return profit
    """

    # Recursion (TLE - 198/200)
    """
    def recursion(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        else:
            maxProfit = float('-inf')

            # sell today
            maxProfit = max(maxProfit, prices[0] - prices[0] + self.recursion(prices[1:]))

            # sell other days
            for index in range(1, len(prices)):
                maxProfit = max(maxProfit, prices[index] - prices[0] + self.recursion(prices[index:]))
            
            return maxProfit

    def maxProfit(self, prices: List[int]) -> int:
        return self.recursion(prices)
    """

    # DP Top Down Memoization, (MLE - 199/200)
    """
    def recursion(self, prices: List[int]) -> int:
        if tuple(prices) in self.memo:
            return self.memo[tuple(prices)]
        if len(prices) == 0:
            return 0
        else:
            maxProfit = float('-inf')

            # sell today
            maxProfit = max(maxProfit, prices[0] - prices[0] + self.recursion(prices[1:]))

            # sell other days
            for index in range(1, len(prices)):
                maxProfit = max(maxProfit, prices[index] - prices[0] + self.recursion(prices[index:]))
            
            self.memo[tuple(prices)] = maxProfit
            return self.memo[tuple(prices)]

    def maxProfit(self, prices: List[int]) -> int:
        self.memo = {}
        return self.recursion(prices)
    """

    # DP Top Down Memoization (TLE - 199/200)
    """
    def recursion(self, index: int) -> int:
        if index in self.memo:
            return self.memo[index]
        if index >= len(self.prices):
            return 0
        else:
            maxProfit = float('-inf')

            # sell today
            maxProfit = max(maxProfit, 0 + self.recursion(index + 1))

            # sell other days
            for idx in range(index+1, len(self.prices)):
                maxProfit = max(maxProfit, self.prices[idx] - self.prices[index] + self.recursion(idx))
            
            self.memo[index] = maxProfit
            return self.memo[index]

    def maxProfit(self, prices: List[int]) -> int:
        self.prices = prices
        self.memo = {}
        return self.recursion(0)
    """
