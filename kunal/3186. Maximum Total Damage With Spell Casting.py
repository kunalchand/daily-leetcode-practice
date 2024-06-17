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
# Similar to 740. Delete and Earn - https://leetcode.com/problems/delete-and-earn/
class Solution:
    # Reference: https://www.twitch.tv/videos/2173278701
    # 2D DP Manual Memoization
    """
    def recursion(self, index: int, oldDamage: int) -> int:
        if (index, oldDamage) in self.memo:
            return self.memo[(index, oldDamage)]

        if index >= len(self.power):
            return 0
        else:
            maxPower = 0

            # Damage
            if not (self.power[index] == oldDamage + 1 or self.power[index] == oldDamage + 2):
                maxPower = max(maxPower, self.power[index] + self.recursion(index + 1, self.power[index]))

            # No Damage
            maxPower = max(maxPower, self.recursion(index + 1, max(oldDamage, self.power[index] - 3)))
            # Refer twitch stream to know why -3 (for fixing MLE)

            self.memo[(index, oldDamage)] = maxPower
            return self.memo[(index, oldDamage)]

    def maximumTotalDamage(self, power: List[int]) -> int:
        self.power = sorted(power)
        self.memo = {}
        return self.recursion(0, -inf)
    """

    # Reference: https://www.twitch.tv/videos/2173278701
    # 2D DP Automatic Memoization
    """
    @cache # or @lru_cache(None)
    def recursion(self, index: int, oldDamage: int) -> int:
        if index >= len(self.power):
            return 0
        else:
            maxPower = 0

            # Damage
            if not (self.power[index] == oldDamage + 1 or self.power[index] == oldDamage + 2):
                maxPower = max(maxPower, self.power[index] + self.recursion(index + 1, self.power[index]))
                
            # No Damage
            maxPower = max(maxPower, self.recursion(index + 1, max(oldDamage, self.power[index] - 3)))
            # Refer twitch stream to know why -3 (for fixing MLE)

            return maxPower

    def maximumTotalDamage(self, power: List[int]) -> int:
        self.power = sorted(power)
        return self.recursion(0, -inf)
    """

    # 1D DP Automatic Memoization
    @cache  # or @lru_cache(None)
    def recursion(self, index: int) -> int:
        if index >= len(self.powers):
            return 0
        else:
            # Damage
            power, freq = self.powers[index]
            damage = power * freq
            if index + 1 < len(self.powers) and (
                self.powers[index + 1][0] != power + 1
                and self.powers[index + 1][0] != power + 2
            ):
                damage += self.recursion(index + 1)
            elif (
                index + 2 < len(self.powers) and self.powers[index + 2][0] != power + 2
            ):
                damage += self.recursion(index + 2)
            else:
                damage += self.recursion(index + 3)

            # No Damage
            noDamage = self.recursion(index + 1)

            return max(damage, noDamage)

    def maximumTotalDamage(self, power: List[int]) -> int:
        self.powers = sorted(Counter(power).items())
        return self.recursion(0)
