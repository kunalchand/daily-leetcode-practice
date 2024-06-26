"""
3075. Maximize Happiness of Selected Children

You are given an array happiness of length n, and a positive integer k.

There are n children standing in a queue, where the ith child has happiness value happiness[i]. 
You want to select k children from these n children in k turns.

In each turn, when you select a child, the happiness value of all the children that have not been selected till now decreases by 1. 
Note that the happiness value cannot become negative and gets decremented only if it is positive.

Return the maximum sum of the happiness values of the selected children you can achieve by selecting k children.

Example 1:
Input: happiness = [1,2,3], k = 2

O (k * log n) + O (n)

happiness = [0,2]

[0,1,0,0]   k = 3

res = 5 + 3 + 1

res = a - 0 + b - 1 + c - 2 + d - 3 


res = 2 + 2 = 4

Output: 4
Explanation: We can pick 2 children in the following way:
- Pick the child with the happiness value == 3. The happiness value of the remaining children becomes [0,1].
- Pick the child with the happiness value == 1. The happiness value of the remaining child becomes [0]. Note that the happiness value cannot become less than 0.
The sum of the happiness values of the selected children is 3 + 1 = 4.

Example 2:
N/A

Example 3:
N/A

Constraints:
N/A
"""

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


class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        max_heap = [-x for x in happiness]
        res = 0 

        heapq.heapify(max_heap)
        
        for i in k:
            if max_heap[0] != 0:
                top = -heapq.heappop(max_heap)
                res += top - i

        return res
    

# [6,5,3,1], k = 4 i = 3
# [0]
# 6 + 4 + 1 + 0 - 3



# res = (6 - 0) + (5 - 1) + (3 - 2) = 6 + 4 + 1 = 11