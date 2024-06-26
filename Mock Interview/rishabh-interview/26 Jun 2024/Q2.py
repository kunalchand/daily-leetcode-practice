"""
1678. Goal Parser Interpretation
https://leetcode.com/problems/goal-parser-interpretation/description/

You own a Goal Parser that can interpret a string command. 
The command consists of an alphabet of "G", "()" and/or "(al)" in some order.
The Goal Parser will interpret "G" as the string "G", "()" as the string "o", and "(al)" as the string "al". 
The interpreted strings are then concatenated in the original order.

Given the string command, return the Goal Parser's interpretation of command.

1
100




str.replace("()", "o")

Example 1:               *
Input: command = "G()(al)"
Output: "Goal"
    Explanation: The Goal Parser interprets the command as follows:
    G -> G
    () -> o
    (al) -> al
    The final concatenated result is "Goal".

Example 2:
Input: command = "G()()()()(al)"
Output: "Gooooal"
"""

import bisect
import copy
import heapq
import math
import random
from bisect import bisect, bisect_left, bisect_right, insort, insort_left, insort_right
from collections import Counter, defaultdict, deque
from dataclasses import dataclass
from functools import cache, cmp_to_key, lru_cache, reduce
from heapq import heapify, heappop, heappush, heappushpop
from itertools import combinations, pairwise, permutations, zip_longest
from math import ceil, factorial, floor, inf, sqrt
from typing import Deque, Dict, List, Optional, Set, Tuple, Union


'''
              * 
0 1 2 3 4 5 6
G ( ) ( a l )

out = Goal
'''

class Solution:
    def interpret(self, command: str) -> str:
        N = len(command)
        res = []
                
        i = 0
        while i < N:
            if command[i] == "(":
                if command[i + 1] == ")":
                    res.append("o")
                    i += 1
                else:
                    res.append("al")
                    i += 3
            else:
                res.append("G")
            
            i += 1
        
        return "".join(res)
        
