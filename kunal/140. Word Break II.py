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


# https://leetcode.com/problems/word-break-ii/
class Solution:
    # Recursion
    """
    def recursion(self, s: str) -> Tuple[List[str], bool]:
        if s == "":
            return ([""], True)

        possibleSentences = []
        for index in range(1, len(s) + 1):
            if s[:index] in self.wordSet:
                sentenceList, validity = self.recursion(s[index:])
                if validity:
                    for sentence in sentenceList:
                        if sentence == "":
                            possibleSentences += [s[:index]]
                        else:
                            possibleSentences += [s[:index] + " " + sentence]

        if possibleSentences:
            return (possibleSentences, True)
        else:
            return ([], False)

    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        self.wordSet = set(wordDict)

        sentenceList, validity = self.recursion(s)

        if validity:
            return sentenceList
        else:
            return []
    """

    # DP, Top Down Memoization
    def recursion(self, s: str) -> Tuple[List[str], bool]:
        if s == "":
            return ([""], True)

        possibleSentences = []
        for index in range(1, len(s) + 1):
            if s[:index] in self.wordSet:
                if s[index:] not in self.memo:
                    self.memo[s[index:]] = self.recursion(s[index:])
                sentenceList, validity = self.memo[s[index:]]
                if validity:
                    for sentence in sentenceList:
                        if sentence == "":
                            possibleSentences += [s[:index]]
                        else:
                            possibleSentences += [s[:index] + " " + sentence]

        if possibleSentences:
            return (possibleSentences, True)
        else:
            return ([], False)

    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        self.wordSet = set(wordDict)
        self.memo = {}

        sentenceList, validity = self.recursion(s)

        if validity:
            return sentenceList
        else:
            return []


print(Solution().wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"]))
print(
    Solution().wordBreak(
        "pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"]
    )
)
print(Solution().wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))
