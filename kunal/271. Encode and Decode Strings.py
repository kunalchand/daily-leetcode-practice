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


# Time-O(n*n*k) Space-O(n) n=strs.length k=strs[i].length
class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string."""
        self.chopLength = []
        ans = ""
        for str_ in strs:
            self.chopLength.append(len(str_))
            ans += str_
        return ans

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings."""
        ans = []
        for chop in self.chopLength:
            ans.append(s[:chop])
            s = s[chop:]
        return ans


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))

codec = Codec()
print(codec.decode(codec.encode(["Hello", "World"])))
print(codec.decode(codec.encode([""])))
