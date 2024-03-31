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
    # Time-O(n) Space-O(2n) [idx-1 * idx+1]
    """
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]*len(nums)
        suffix = [1]*len(nums)

        for index in range(len(nums)):
            if index == 0:
                prefix[index] = 1 * nums[index]
            else:
                prefix[index] = prefix[index-1] * nums[index]

        for index in range(len(nums)-1, -1, -1):
            if index == len(nums)-1:
                suffix[index] = nums[index] * 1
            else:
                suffix[index] = nums[index] * suffix[index+1]

        ans = [1]*len(nums)

        for index in range(len(nums)):
            if index == 0:
                ans[index] = 1 * suffix[index+1]
            elif index == len(nums)-1:
                ans[index] = prefix[index-1] * 1
            else:
                ans[index] = prefix[index-1] * suffix[index+1]

        return ans
    """

    # Time-O(n) Space-O(2n) [idx * idx]
    """
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]*len(nums)
        suffix = [1]*len(nums)

        for index in range(1, len(nums)):
            prefix[index] = prefix[index-1] * nums[index-1]
        
        for index in range(len(nums)-2, -1, -1):
            suffix[index] = nums[index+1] * suffix[index+1]

        ans = [1]*len(nums)
        
        for index in range(len(nums)):
            ans[index] = prefix[index]*suffix[index]
        
        return ans
    """

    # Time-O(n) Space-O(1)
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)

        for index in range(1, len(nums)):
            prefix[index] = prefix[index - 1] * nums[index - 1]

        suffix_product = 1

        for index in range(len(nums) - 1, -1, -1):
            prefix[index] *= suffix_product
            suffix_product *= nums[index]

        return prefix


print(Solution().productExceptSelf([1, 2, 3, 4]))
print(Solution().productExceptSelf([-1, 1, 0, -3, 3]))
