"""
735. Asteroid Collision

We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign 
represents its direction (positive meaning right, negative meaning left). 
Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. 
If two asteroids meet, the smaller one will explode. 
If both are the same size, both will explode. 
Two asteroids moving in the same direction will never meet.

2 to 10 ^ 4

APPROACH: 
    1. Brute Force => O(n ** 2)

[5 , - 5] => []

# collide
[10, -5] => [10]

# never collide
    [-5, 10] => [-5, 10] 
    [10, 5] or [-10, -5]


[1, 2, -10] => [1, -10] => [-10]


[a, B, c, d, e, -f, -G]         => e - f
[a, b, c, d, -f]                => d - f
[a, b, c, -f]                   => c - f
.
[a ,B, -G]
.
[-f]


[a, B, c, d, e, -f]
[a, B, c, D, B]
[a, B]


[a, B, c, d, E || -f, -G]

[a, B, c, d || -f, -G] or [a, B, c, d, e || -G]




[a, B, c, d, -f, -G]

[-G]

Example 1:
Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.

Example 2:
Input: asteroids = [8,-8]
Output: []
Explanation: The 8 and -8 collide exploding each other.

Example 3:
Input: asteroids = [10,2,-5]
Output: [10]
Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.

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
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # Write your code here
        pass
