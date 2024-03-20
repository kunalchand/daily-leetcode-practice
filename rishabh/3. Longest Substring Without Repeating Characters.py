class Solution:

    '''
    I/P:
        str (any char)
    O/P:
        len(substring without repeatition)

    clarifying question:
        uppercase and lower case are different
        digit, symbol, spaces, any char
        
        substring? => contiguous subarray

    Edge case:
        "" => 0

    Approaches:
        1. Brute Force:
            TIME: O(N ^ 2), SPACE: O(1)
            use a set and make a chain
            "abcde" worst case
            "aaaaa" best case
        
        2. make sliding window of unique chars
            TIME: O(N), SPACE: O(N), set
            set(), remove until repeated char is removed

            xyzaabcabcbb
            ""
            abcd
            aaaa

            max_len = 1
            set = ( a )
    
    '''
    '''
    APPROACH-1: SLIDING WINDOW
    TIME AND SPACE: O(N)
    '''
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        window_chars = set()

        l, r = 0, 0
        while r < len(s):                           # stop when r reaches end of s
            while s[r] in window_chars:             # duplicate char, remove elements and shrink window
                window_chars.remove(s[l])
                l += 1

            window_chars.add(s[r])                  # unique char => add to set and grow window
            max_len = max(max_len, r - l + 1)       # check size
            r += 1                                  # move right pointer

        return max_len

    '''
    APPROACH: BRUTE FORCE using hashset
    TIME: O(N ^ 2)
    SPACE: O(N)
    '''
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0

        for i in range(len(s)):
            window_chars = set()   

            for j in range(i, len(s)):
                if s[j] not in window_chars:
                    window_chars.add(s[j])
                    max_len = max(max_len, len(window_chars))         
                else:
                    break

        return max_len


    '''
    SLIDING WINDOW EXPLANATION
    set : it'll contain the current window chars
    if incoming char already present in set, 
    keep removing chars from set that s[l] points 
    till occurace of incoming duplicate char is also removed
    make window shrink by keep incrementing left pointer
    TIME: O(N), traversing through array
    SPACE: O(N), set used to check duplicates
    '''
