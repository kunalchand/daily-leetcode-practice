class Solution:
    '''
    APPROACH-1: Brute force
    Check every possible sub-string from starting to end
    TIME: O(N ^ 3)
    SPACE: O(1)
    '''
    def countSubstrings(self, s: str) -> int:
        def is_palindrome(sbs):                                             # T(N) = O (N)
            return sbs == sbs[::-1]
        res = []
        # T(N) = O (N ^ 3)
        for i in range(len(s)):                                             # T(N) = O (N)
            for j in range(i+1, len(s)):                                    # T(N) = O (N)
                substring = s[i : j + 1]
                if(is_palindrome(substring)): res.append(substring)         # T(N) = O (N)
        print(res)
        return len(s) + len(res)
     
        

    '''
    APPROACH-2: expand around every possible center
    odd length (single char center) and 
    even length palindromes (consecutive char center)
    TIME: O(N ^ 2)
    SPACE: O(1)
    '''    
    def countSubstrings(self, s: str) -> int:
        # T(N) = O(N)
        def count_palindrome(left, right):
            curr_count = 0
            while 0 <= left and right < len(s) and s[left] == s[right]:
                curr_count += 1
                left, right = left - 1, right + 1
            return curr_count

        ans = 0
        # T(N) = O(N ^ 2)
        for i in range(len(s)):                      # T(N) = O(N)
            ans += count_palindrome(i, i)            # odd length (single char center)
            ans += count_palindrome(i, i + 1)        # even length palindromes (consecutive char center)
        return ans