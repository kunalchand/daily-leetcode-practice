"""
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
 

Example 1:

Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.
Example 2:

Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.
 

Constraints:

0 <= x <= 2^31 - 1

Brute Force:
0 1 2 3 ... a b

Binary Search
0 ... mid mid+1 mid+2 mid+3... x
"""


class Solution:
    # Brute Force TIme-O(sqrt(n)) Space-O(1)
    """
    def mySqrt(self, x: int) -> int:
        sqrt = 0
        val = 0

        while val * val <= x:
            sqrt = val
            val += 1

        return sqrt
    """

    # Binary Search Time-O(log n) Space-O(1)
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x

        ans = -1

        while left <= right:
            mid = (left + right) // 2

            if mid * mid <= x:
                ans = mid
                left = mid + 1  # Ignore the left half
            else:
                right = mid - 1  # Ignore the right half

        return ans


print(Solution().mySqrt(4))
print(Solution().mySqrt(25))
print(Solution().mySqrt(26))
