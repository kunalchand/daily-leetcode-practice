import copy
import heapq
import math
import random
from collections import Counter, defaultdict, deque
from dataclasses import dataclass
from functools import cmp_to_key, reduce
from itertools import zip_longest
from math import factorial, sqrt
from typing import Dict, List, Optional, Tuple, Union


class Solution:
    # O(n*n) [Gives TLE]
    """
    class Element:
        def __init__(self, char: str, count: int):
            self.char = char
            self.count = count

        def __lt__(self, other):
            return self.count > other.count

        def __repr__(self):
            return "(" + str(self.char) + ", " + str(self.count) + ")"

    def heapSetup(self, tasks: List[str], maxHeap: List["Solution.Element"]) -> None:
        dict_ = {}

        for task in tasks:
            dict_[task] = dict_.get(task, 0) + 1

        for char, count in dict_.items():
            heapq.heappush(maxHeap, Solution.Element(char, count))

    def mergeHeap(self, maxHeap, storeHeap) -> None:
        maxHeap.extend(storeHeap)
        storeHeap.clear()
        heapq.heapify(maxHeap)

    def leastInterval(self, tasks: List[str], n: int) -> int:
        maxHeap = []
        storeHeap = []
        self.heapSetup(tasks, maxHeap)

        resultList = []

        while maxHeap:
            flag = "idle"
            while maxHeap:
                topElement = heapq.heappop(maxHeap)
                topChar = topElement.char
                if topChar not in resultList or resultList.index(topChar) >= n:
                    flag = "occupied"
                    resultList.insert(0, topChar)
                    topElement.count -= 1
                    if topElement.count != 0:
                        heapq.heappush(maxHeap, topElement)
                    self.mergeHeap(maxHeap, storeHeap)
                    break
                else:
                    storeHeap.append(topElement)

            if flag == "idle":
                resultList.insert(0, "idle")
                self.mergeHeap(maxHeap, storeHeap)

        print(list(reversed(resultList)))
        return len(resultList)
    """

    # O(n logn)
    class Element:
        def __init__(self, char: str, count: int):
            self.char = char
            self.count = count

        def __lt__(self, other):
            return self.count > other.count

        def __repr__(self):
            return "(" + str(self.char) + ", " + str(self.count) + ")"

    def heapSetup(self, tasks: List[str], maxHeap: List["Solution.Element"]) -> None:
        dict_ = {}

        for task in tasks:
            dict_[task] = dict_.get(task, 0) + 1

        for char, count in dict_.items():
            heapq.heappush(maxHeap, Solution.Element(char, count))

    def useTaskAndApplyCooldown(self, maxHeap, cooldown, ansList, n):
        topElement = heapq.heappop(maxHeap)
        ansList.append(topElement.char)
        topElement.count -= 1
        if topElement.count != 0:
            for _ in range(len(cooldown), n):
                cooldown.append(Solution.Element("idle", -1))
            cooldown.append(topElement)

    def leastInterval(self, tasks: List[str], n: int) -> int:
        maxHeap = []
        self.heapSetup(tasks, maxHeap)

        ansList = []
        cooldown = deque()
        while True:
            if not maxHeap and not cooldown:
                break

            elif maxHeap and not cooldown:
                self.useTaskAndApplyCooldown(maxHeap, cooldown, ansList, n)

            elif maxHeap and cooldown:
                exitElement = cooldown[0]
                if exitElement.char == "idle":
                    cooldown.popleft()
                else:
                    heapq.heappush(maxHeap, cooldown.popleft())

                self.useTaskAndApplyCooldown(maxHeap, cooldown, ansList, n)

            elif not maxHeap and cooldown:
                exitElement = cooldown[0]
                if exitElement.char == "idle":
                    cooldown.popleft()
                    ansList.append("idle")
                else:
                    heapq.heappush(maxHeap, cooldown.popleft())
                    self.useTaskAndApplyCooldown(maxHeap, cooldown, ansList, n)

        return len(ansList)


print(Solution().leastInterval(["A", "A", "A", "B", "B", "B"], 2))
print(Solution().leastInterval(["A", "C", "A", "B", "D", "B"], 1))
print(Solution().leastInterval(["A", "A", "A", "B", "B", "B"], 3))
print(Solution().leastInterval(["A", "B", "C", "A"], 2))
