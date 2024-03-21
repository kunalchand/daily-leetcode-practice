import copy
import heapq
import math
import random
from collections import Counter, defaultdict, deque
from dataclasses import dataclass
from functools import cmp_to_key, reduce
from itertools import zip_longest
from math import factorial, sqrt
from typing import Dict, List, Optional, Set, Tuple, Union


class Solution:
    # Brute Force O(Exponential) by array slice
    """
    def canJump(self, nums: List[int]) -> bool:
        # Landed on Last Index
        if len(nums) == 1:
            return True
        else:
            jump = nums[0]

            # Lands on Zero
            if jump == 0:
                return False
            # Can Jump to Last Index
            elif jump >= len(nums)-1:
                return True
            # Explore All Jumps
            else:
                flag = False
                while jump > 0:
                    flag = flag or self.canJump(nums[jump:])
                    jump -= 1
                return flag
    """

    # Brute Force O(Exponential) by index
    """
    def makeTrip(self, nums: List[int], index: int) -> bool:
        # Landed on Last Index
        if index == len(nums)-1:
            return True
        else:
            jump = nums[index]
            
            # Lands on Zero
            if jump == 0:
                return False
            # Can Jump to Last Index
            elif index + jump >= len(nums) - 1:
                return True
            # Explore All Jumps
            else:
                flag = False
                while jump > 0:
                    flag = flag or self.makeTrip(nums, index + jump)
                    jump -= 1
                return flag

    def canJump(self, nums: List[int]) -> bool:
        return self.makeTrip(nums, 0)
    """

    # DP Top Down Memoization Approach Time-O(?) Space-O(?)
    """
    def makeTrip(self, nums: List[int], index: int) -> bool:
        # Landed on Last Index
        if index == len(nums)-1:
            return True
        else:
            jump = nums[index]
            
            # Lands on Zero
            if jump == 0:
                return False
            # Can Jump to Last Index
            elif index + jump >= len(nums) - 1:
                return True
            # Explore All Jumps
            else:
                flag = False
                while jump > 0:
                    isItPossible = False
                    if index + jump in self.memoization:
                        isItPossible = self.memoization[index + jump]
                    else:
                        isItPossible = self.makeTrip(nums, index + jump)
                        self.memoization[index + jump] = isItPossible
                    flag = flag or isItPossible
                    jump -= 1
                return flag

    def canJump(self, nums: List[int]) -> bool:
        self.memoization = {}
        return self.makeTrip(nums, 0)
    """

    # DP Bottom Up Approach Time-O(?) Space-O(n)
    """
    def canJump(self, nums: List[int]) -> bool:
        dp = [False] * len(nums)
        dp[-1] = True

        for index in range(len(dp)-2, -1, -1):
            jump = nums[index]
            if index + jump >= len(nums)-1:
                dp[index] = True
            else:
                while jump > 0:
                    dp[index] = dp[index] or dp[index + jump]
                    jump -= 1

        return dp[0]
    """

    # Greedy Approach Time-O(n) Space-O(1)
    def findStart(self, nums: List[int], finish: int) -> int:
        start = finish - 1

        while start > -1:
            if nums[start] >= finish - start:
                return start
            start -= 1

        return -1

    def canJump(self, nums: List[int]) -> bool:
        finish = len(nums) - 1

        while finish > 0:
            start = self.findStart(nums, finish)
            if start == -1:
                return False
            finish = start

        return True
