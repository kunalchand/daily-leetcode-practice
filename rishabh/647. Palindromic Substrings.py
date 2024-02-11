class Solution:
    def countSubstrings(self, s: str) -> int:
        '''
        APPROACH: Brute force
        Check every possible sub-string from starting to end
        TIME: O(N ^ 3)
        SPACE: O(1)
        '''
        def is_palindrome(sbs):
            return sbs == sbs[::-1]
        res = []
        for i in range(len(s)):
            for j in range(i+1, len(s)):
                substring = s[i : j + 1]
                if(is_palindrome(substring)): res.append(substring)
        print(res)
        return len(s) + len(res)
        