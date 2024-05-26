"""
2810. Faulty Keyboard

Your laptop keyboard is faulty, and 
whenever you type a character 'i' on it, 
it reverses the string that you have written. 
Typing other characters works as expected.

You are given a 0-indexed string s, and 
you type each character of s using your 
faulty keyboard.

Return the final string that will be 
present on your laptop screen.

Example 1:
Input: s = "string"
Output: "rtsng"
Explanation: 
    After typing first character, the text on the screen is "s".
    After the second character, the text is "st". 
    After the third character, the text is "str".
    Since the fourth character is an 'i', the text gets reversed and becomes "rts".
    After the fifth character, the text is "rtsn". 
    After the sixth character, the text is "rtsng". 
    Therefore, we return "rtsng".

Example 2:
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
    def finalString(self, s: str) -> str:
        pass
