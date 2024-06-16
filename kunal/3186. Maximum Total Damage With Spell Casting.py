import bisect
import copy
import heapq
import math
import random
from bisect import bisect, bisect_left, bisect_right, insort, insort_left, insort_right
from collections import Counter, defaultdict, deque
from dataclasses import dataclass
from functools import cache, cmp_to_key, lru_cache, reduce
from itertools import combinations, pairwise, permutations, zip_longest
from math import ceil, factorial, floor, inf, sqrt
from typing import Dict, List, Optional, Set, Tuple, Union


# https://leetcode.com/problems/maximum-total-damage-with-spell-casting/
class Solution:
    # Reference: https://www.twitch.tv/videos/2173278701
    # Manual Memoization
    """
    def recursion(self, index: int, oldDamage: int) -> int:
        if (index, oldDamage) in self.memo:
            return self.memo[(index, oldDamage)]

        if index >= len(self.power):
            return 0
        else:
            # Can't Damage
            if self.power[index] == oldDamage + 1 or self.power[index] == oldDamage + 2:
                self.memo[(index, oldDamage)] = self.recursion(index + 1, oldDamage)
                return self.memo[(index, oldDamage)]

            # Can Damage
            # Damage
            maxPower = max(self.power[index], self.power[index] + self.recursion(index + 1, self.power[index]))
            # No Damage
            maxPower = max(maxPower, self.recursion(index + 1, max(oldDamage, self.power[index] - 3)))
            # Refer twitch to know why max and how to fix MLE

            self.memo[(index, oldDamage)] = maxPower
            return self.memo[(index, oldDamage)]

    def maximumTotalDamage(self, power: List[int]) -> int:
        self.power = sorted(power)
        self.memo = {}
        return self.recursion(0, -inf)
    """

    # Reference: https://www.twitch.tv/videos/2173278701
    # Automatic Memoization
    @cache  # or @lru_cache(None)
    def recursion(self, index: int, oldDamage: int) -> int:
        if index >= len(self.power):
            return 0
        else:
            # Can't Damage
            if self.power[index] == oldDamage + 1 or self.power[index] == oldDamage + 2:
                return self.recursion(index + 1, oldDamage)

            # Can Damage
            # Damage
            maxPower = max(
                self.power[index],
                self.power[index] + self.recursion(index + 1, self.power[index]),
            )
            # No Damage
            maxPower = max(
                maxPower,
                self.recursion(index + 1, max(oldDamage, self.power[index] - 3)),
            )
            # Refer twitch to know why max and how to fix MLE

            return maxPower

    def maximumTotalDamage(self, power: List[int]) -> int:
        self.power = sorted(power)
        return self.recursion(0, -inf)
