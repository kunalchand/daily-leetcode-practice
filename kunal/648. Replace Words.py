import bisect
import copy
import heapq
import math
import random
from bisect import bisect, bisect_left, bisect_right, insort, insort_left, insort_right
from collections import Counter, defaultdict, deque
from dataclasses import dataclass
from functools import cmp_to_key, reduce
from itertools import combinations, pairwise, permutations, zip_longest
from math import ceil, factorial, floor, sqrt
from typing import Dict, List, Optional, Set, Tuple, Union


# https://leetcode.com/problems/replace-words/
class Solution:
    # HashMap
    """
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        dictionary = set(dictionary)

        words = sentence.split(" ")

        for index, word in enumerate(words[:]):
            for length in range(1, len(word)+1):
                if word[:length] in dictionary:
                    words[index] = word[:length]
                    break

        return " ".join(words)
    """

    # Trie
    class TrieNode:
        def __init__(self) -> None:
            self.children = {}
            self.isRoot = False
            self.root = None

    class Trie:
        def __init__(self) -> None:
            self.zeroLevel = {}

        def addRoot(self, root: str) -> None:
            word = root
            level = self.zeroLevel
            letter = word[0]
            while True:
                level.setdefault(letter, Solution.TrieNode())
                if len(word) == 1:
                    level[letter].isRoot = True
                    level[letter].root = root
                word = word[1:]
                if word == "":
                    break
                level = level[letter].children
                letter = word[0]

        def getRoot(self, word: str) -> str:
            originalWord = word
            level = self.zeroLevel
            letter = word[0]
            while True:
                if letter in level:
                    trieNode = level[letter]
                    if trieNode.isRoot:
                        return trieNode.root
                    word = word[1:]
                    if word == "":
                        return originalWord
                    level = level[letter].children
                    letter = word[0]
                else:
                    return originalWord

    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        self.dictionary = list(set(dictionary))
        self.trie = Solution.Trie()

        for root in self.dictionary:
            self.trie.addRoot(root)

        words = sentence.split(" ")

        for index, word in enumerate(words[:]):
            words[index] = self.trie.getRoot(word)

        return " ".join(words)
