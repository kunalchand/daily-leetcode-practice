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


# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
class Solution:
    # Brute Force Time-O(n*n) Space-O(1)
    """
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                buy = prices[i]
                sell = prices[j]
                max_profit = max(max_profit, sell - buy)

        return max_profit
    """

    # Suffix Max Time-O(n) Space-O(n)
    """
    def maxProfit(self, prices: List[int]) -> int:
        suffix_max = [0] * (len(prices)-1)

        for i in range(len(suffix_max)-1, -1, -1):
            if i == len(suffix_max)-1:
                suffix_max[i] = prices[i+1]
            else:
                suffix_max[i] = max(prices[i+1], suffix_max[i+1])

        max_profit = 0

        for i in range(len(suffix_max)):
            buy = prices[i]
            sell = suffix_max[i]
            max_profit = max(max_profit, sell - buy)
        
        return max_profit
    """

    # Running Max Time-O(n) Space-O(1)
    """
    def maxProfit(self, prices: List[int]) -> int:
        sell = prices[-1]
        max_profit = 0

        i = len(prices)-2

        while i >= 0:
            buy = prices[i]
            max_profit = max(max_profit, sell - buy)
            sell = max(sell, prices[i])
            i -= 1
        
        return max_profit
    """

    # Sliding Window Time-O(n) Space-O(1)
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        b, s = 0, 0

        while s < len(prices):
            buy = prices[b]
            sell = prices[s]

            if buy == sell:
                s += 1
            elif buy > sell:
                b = s
            else:
                max_profit = max(max_profit, sell - buy)
                s += 1

        return max_profit


print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))
print(Solution().maxProfit([7, 6, 4, 3, 1]))
