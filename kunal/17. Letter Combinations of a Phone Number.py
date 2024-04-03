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
    # Recursion SubProblem Approach
    """
    def generateCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        else:
            combinations = []

            for letter in self.hashmap[digits[0]]:
                for subCombination in self.generateCombinations(digits[1:]) or ['']:
                    combinations.append(letter + subCombination)

            return combinations


    def letterCombinations(self, digits: str) -> List[str]:
        self.hashmap = defaultdict(list)

        self.hashmap["2"].extend(["a", "b", "c"])
        self.hashmap["3"].extend(["d", "e", "f"])
        self.hashmap["4"].extend(["g", "h", "i"])
        self.hashmap["5"].extend(["j", "k", "l"])
        self.hashmap["6"].extend(["m", "n", "o"])
        self.hashmap["7"].extend(["p", "q", "r", "s"])
        self.hashmap["8"].extend(["t", "u", "v"])
        self.hashmap["9"].extend(["w", "x", "y", "z"])

        return self.generateCombinations(digits)
    """

    # Recursion Tree Approach
    def generateCombinations(self, digits: str, current: str) -> None:
        if len(digits) == 0:
            if len(current) > 0:
                self.ans.append(current)
        else:
            for letter in self.hashmap[digits[0]]:
                self.generateCombinations(digits[1:], current + letter)

    def letterCombinations(self, digits: str) -> List[str]:
        self.hashmap = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

        self.ans = []

        self.generateCombinations(digits, "")

        return self.ans


print(Solution().letterCombinations("23"))
print(Solution().letterCombinations(""))
print(Solution().letterCombinations("2"))
