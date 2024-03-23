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
    # Brute Force Time-O(Exponetial) using index
    """
    def makeTrip(self, nums: List[int], index: int) -> int:
        # landed on the last index
        if index == len(nums)-1:
            return 0
        else:
            jump = nums[index]

            # landed on 0
            if jump == 0:
                return float('inf')
            # can land on last index
            elif index + jump >= len(nums)-1:
                return 1
            # explore all jumps
            else:
                totalJumps = float('inf')
                while jump > 0:
                    totalJumps = min(totalJumps, self.makeTrip(nums, index + jump))
                    jump -= 1
                return 1 + totalJumps

    def jump(self, nums: List[int]) -> int:
        return self.makeTrip(nums, 0)
    """

    # DP Top Down Memoization Approach Time-O(?) Space-O(?)
    """
    def makeTrip(self, nums: List[int], index: int) -> int:
        # landed on the last index
        if index == len(nums)-1:
            return 0
        else:
            jump = nums[index]

            # landed on 0
            if jump == 0:
                return float('inf')
            # can land on last index
            elif index + jump >= len(nums)-1:
                return 1
            # explore all jumps
            else:
                totalJumps = float('inf')
                while jump > 0:
                    tripSteps = 0
                    if index + jump not in self.memoization:
                        self.memoization[index + jump] = self.makeTrip(nums, index + jump)
                    tripSteps = self.memoization[index + jump]

                    totalJumps = min(totalJumps, tripSteps)
                    jump -= 1
                return 1 + totalJumps

    def jump(self, nums: List[int]) -> int:
        self.memoization = {}
        return self.makeTrip(nums, 0)
    """

    # DP Bottom Up Approach Time-O(n*n) Space-O(n)
    """
    def jump(self, nums: List[int]) -> int:
        dp = [float('inf')] * len(nums)
        dp[-1] = 0

        for index in range(len(nums)-2, -1, -1):
            jump = nums[index]
            while jump > 0:
                if index + jump < len(nums):
                    dp[index] = min(dp[index], dp[index + jump])
                else:
                    dp[index] = min(dp[index], 0)
                jump -= 1
            dp[index] += 1

        return dp[0]
    """

    # Greedy Time-O(n*n) Space-O(1)
    """
    def findStart(self, nums: List[int], finish: int) -> int:
        earlyStart = finish - 1
        start = finish - 1
        
        while start >= 0:
            jump = start + nums[start]
            if jump >= finish:
                earlyStart = start
            start -= 1

        return earlyStart

    def jump(self, nums: List[int]) -> int:
        totalJumps = 0

        finish = len(nums) - 1

        while finish > 0:
            start = self.findStart(nums, finish)
            finish = start
            totalJumps += 1
        
        return totalJumps
    """

    # Greedy Time-O(n) Space-O(1) using class
    """
    class Level:
        def __init__(self, start, end):
            self.start = start
            self.end = end
        
        def __repr__(self):
            return "({}, {})".format(str(self.v1), str(self.v2))

    def jump(self, nums: List[int]) -> int:
        totalJumps = 0

        currentLevel = Solution.Level(0, 0)

        while not currentLevel.start <= len(nums)-1 <= currentLevel.end:
            nextLevel = Solution.Level(currentLevel.end+1, currentLevel.end+1)

            for index in range(currentLevel.start, currentLevel.end+1):
                jump = nums[index]
                nextLevel.end = max(nextLevel.end, index+jump)

            currentLevel = nextLevel
            totalJumps += 1
        
        return totalJumps
    """

    # Greedy Time-O(n) Space-O(1) without class
    def jump(self, nums: List[int]) -> int:
        totalJumps = 0

        currentLevel = [0, 0]

        while not currentLevel[0] <= len(nums) - 1 <= currentLevel[1]:
            nextLevel = [currentLevel[1] + 1, currentLevel[1] + 1]

            for index in range(currentLevel[0], currentLevel[1] + 1):
                jump = nums[index]
                nextLevel[1] = max(nextLevel[1], index + jump)

            currentLevel = nextLevel
            totalJumps += 1

        return totalJumps


print(Solution().jump([2, 3, 1, 1, 4]))
print(Solution().jump([2, 3, 0, 1, 4]))
