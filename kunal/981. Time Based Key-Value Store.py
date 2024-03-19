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

# O(n*logm) Using User Defined Class
"""
class Block:
    def __init__(self, value: str, timestamp: int):
        self.value = value
        self.timestamp = timestamp
    
    def __repr__(self):
        return "(" + self.value + ", " + str(self.timestamp) + ")"

class TimeMap:

    def __init__(self):
        self.box = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.box[key].append(Block(value, timestamp))

    def linearSearch(self, searchList: List["Block"], timestamp: int, left: int, right: int) -> str:
        searchValue = ""

        while left <= right:
            if searchList[left].timestamp <= timestamp:
                searchValue = searchList[left].value
            else:
                break
            left += 1
        
        return searchValue

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.box:
            return ""

        searchList = self.box[key]

        left, right = 0, len(searchList)-1
            
        while True:
            if right - left < 3:
                return self.linearSearch(searchList, timestamp, left, right)
            else:
                mid = (left + right)//2

                if searchList[mid].timestamp == timestamp:
                    return searchList[mid].value
                elif timestamp < searchList[mid].timestamp:
                    right = mid - 1
                elif searchList[mid].timestamp < timestamp:
                    left = mid + 1

        return ""    


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
"""


# O(n*logm) Using Tuple
class TimeMap:

    def __init__(self):
        self.box = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.box[key].append((value, timestamp))

    def linearSearch(
        self, searchList: List[Tuple], timestamp: int, left: int, right: int
    ) -> str:
        searchValue = ""

        while left <= right:
            if searchList[left][1] <= timestamp:
                searchValue = searchList[left][0]
            else:
                break
            left += 1

        return searchValue

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.box:
            return ""

        searchList = self.box[key]

        left, right = 0, len(searchList) - 1

        while True:
            if right - left < 3:
                return self.linearSearch(searchList, timestamp, left, right)
            else:
                mid = (left + right) // 2

                if searchList[mid][1] == timestamp:
                    return searchList[mid][0]
                elif timestamp < searchList[mid][1]:
                    right = mid - 1
                elif searchList[mid][1] < timestamp:
                    left = mid + 1

        return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
