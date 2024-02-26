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


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def createCopyAndInsert(self, cur) -> "Node":
        if cur is None:
            return None

        copyNode = Node(cur.val)
        copyNode.next = self.createCopyAndInsert(cur.next)
        cur.next = copyNode

        return cur

    def setRandomPointer(self, cur) -> None:
        if cur is None:
            return
        else:
            if cur.random is not None:
                cur.next.random = cur.random.next

            self.setRandomPointer(cur.next.next)

    def resetLinks(self, cur) -> Tuple["Node", "Node"]:
        if cur is None:
            return (None, None)

        originalCur, copyCur = cur, cur.next
        originalHead, copyHead = self.resetLinks(cur.next.next)

        originalCur.next = originalHead
        copyCur.next = copyHead

        return (originalCur, copyCur)

    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        self.createCopyAndInsert(head)
        self.setRandomPointer(head)

        originalHead, copyHead = self.resetLinks(head)

        return copyHead
