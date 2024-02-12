from collections import defaultdict
from typing import List


class Solution:
    '''
    APPROACH-1: Use hashmap + char occurance count
    {key : value}
    {occurance of each char from a ... z : list of anagrams}
    { (1,1, ... , 0) : [ab, ba] }
    TIME: O(N * M), N = len(strs), M = max-length/avg-length of str in strs
    SPACE: O(N)
    '''
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # default value for each key is an empty list
        res = defaultdict(list)                # {char_count -> list of anagrams}
        for s in strs:
            count = [0] * 26                   # a,b, ... , z
            for char in s:
                # count[0] will store occurances of 'a'
                # count[1] will store occurances of 'b' and so on
                count[ord(char) - ord('a')] += 1    # ord -> unicode value
        
            # what if count doesn't exist in the res yet?
            # that's why we defined res as defaultdict(list)
            # that's why we are not checking if the count already exist in res yet
            # we can just append 's' to an empty list
            
            # list can't be keys in python, that's why tuple
            # list isn't hashable, tuple/string is
            res[tuple(count)].append(s)

        return res.values()




    '''
    APPROACH-2: Use hashmap + sorting
    {key : value}
    {sorted word : list of anagrams}
    { "aet" : ['eat', 'tea', 'ate'] }
    TIME: O(N * M log M), N = len(strs), M = max-length/avg-length of str in strs
    SPACE: O(N)
    '''
    def groupAnagrams2(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for word in strs:                   # O(N)
            key = "".join(sorted(word))     # O(M * log M)
            # strings can be used as keys in hash tables, lists can't
            # strings are hasable, lists aren't
            if key not in res: res[key] = [word]
            else: res[key].append(word)
        
        return (res.values())