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


# https://leetcode.com/problems/maximum-score-words-formed-by-letters/
class Solution:
    def calculateScore(self, wordFreq: Counter) -> int:
        wordScore = 0
        for letter, freq in wordFreq.items():
            wordScore += self.score[letter] * freq
        return wordScore

    def isValidWord(self, wordFreq: Counter) -> bool:
        for letter, freq in wordFreq.items():
            if letter not in self.letters or freq > self.letters[letter]:
                return False
        return True

    def generateWords(self, words: List[str]) -> None:
        for word in words:
            wordFreq = Counter("".join(word))
            if self.isValidWord(wordFreq):
                wordScore = self.calculateScore(wordFreq)
                self.words.append([word, wordFreq, wordScore])

    def generateScore(self, score: List) -> None:
        alphabets = "abcdefghijklmnopqrstuvwxyz"
        self.score = dict(zip(list(alphabets), score))

    def modifyLetters(self, wordFreq: Counter) -> None:
        for letter, freq in wordFreq.items():
            self.letters[letter] -= freq

    def restoreLetters(self, wordFreq: Counter) -> None:
        for letter, freq in wordFreq.items():
            self.letters[letter] += freq

    def backtrack(self, index: int) -> int:
        if index >= len(self.words):
            return 0

        maxScore = 0
        word, wordFreq, wordScore = self.words[index]

        # Choose
        if self.isValidWord(wordFreq):
            self.modifyLetters(wordFreq)
            maxScore = max(maxScore, wordScore + self.backtrack(index + 1))
            self.restoreLetters(wordFreq)

        # Not Choose
        maxScore = max(maxScore, self.backtrack(index + 1))

        return maxScore

    def maxScoreWords(
        self, words: List[str], letters: List[str], score: List[int]
    ) -> int:
        self.score = {}
        self.generateScore(score)

        self.letters = Counter("".join(letters))

        self.words = []
        self.generateWords(words)

        return self.backtrack(0)


print(
    Solution().maxScoreWords(
        ["dog", "cat", "dad", "good"],
        ["a", "a", "c", "d", "d", "d", "g", "o", "o"],
        [1, 0, 9, 5, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    )
)

print(
    Solution().maxScoreWords(
        ["xxxz", "ax", "bx", "cx"],
        ["z", "a", "b", "c", "x", "x", "x"],
        [4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 10],
    )
)

print(
    Solution().maxScoreWords(
        ["leetcode"],
        ["l", "e", "t", "c", "o", "d"],
        [0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    )
)
