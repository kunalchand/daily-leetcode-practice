class Solution:
    def firstUniqChar(self, s: str) -> int:
        ## Approach-1: brute force
        ## Time: O(n * n)
        ## Space: O(1)
        
        for i in range(len(s)):
            # False flag denotes there is no repitition
            flag = False                     
            for j in range(len(s)):
                if i != j:                          # skip element at the same index
                    if s[i] == s[j]: flag = True    # found a duplicate
            if not flag: return i

        return -1       # all characters repeat


    def firstUniqCharSets(self, s: str) -> int:    
        ## Approach-2: using sets
        ## use 2 sets, 1st to store every new element, 
        ##             2nd to store if an ele occurs again
        ## traverse the list again and return the char that occurs in 1st but not in 2nd 
        ## Time: O(n)
        ## Space: O(n)
        
        first, second = set(), set()

        for c in s:
            if c not in first: first.add(c)         # store every new element in 1st
            elif c in first: second.add(c)          # if an ele occurs again, store in 2nd

        # traverse the list again and return the char that occurs in 1st but not in 2nd     
        for idx,c in enumerate(s):
            if c in first and c not in second:
                return idx
        
        return -1
        
    def firstUniqChar3(self, s: str) -> int:
        ## Approach-3: Using Dictionary
        ## dict preserves order
        ## return the first key where val == 1
        ## Time: O(n)
        ## Space: O(n)
        count = {}      # {char: occurance}
        for c in s:
            count[c] = count.get(c, 0) + 1

        non_repeat_char = ''
        # print(count)

        for k,v in count.items():
            if v == 1:                  # pick the first key for which val is 1
                non_repeat_char = k
                break

        for idx,ele in enumerate(s):      # return above picked key's idx
            if ele == non_repeat_char:
                return idx

        return -1
    
    # short version of firstUniqChar3()
    def firstUniqChar4(self, s: str) -> int:
        count = {}      # {char: occurance}
        for c in s:
            count[c] = count.get(c, 0) + 1

        for idx in range(len(s)):
            if count[s[idx]] == 1: return idx
        
        return -1
    

