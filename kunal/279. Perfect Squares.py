from math import sqrt


class Solution:
    # O(n^2)
    """
    def numSquares(self, n: int) -> int:
        if sqrt(n) % 1 == 0:
            return 1

        dp = [float('inf') for _ in range(n+1)]

        for index in range(1, n+1):
            if sqrt(index) % 1 == 0:
                dp[index] = 1
            else:
                left = index-1
                right = 1
                while left > 0:
                    dp[index] = min(dp[index], dp[left] + dp[right])
                    left -= 1
                    right += 1

        return dp[-1]
    """

    # O(n*sqrt(n))
    def numSquares(self, n: int) -> int:
        if sqrt(n) % 1 == 0:
            return 1

        dp = [float("inf") for _ in range(n + 1)]
        dp[0] = 0

        for num in range(1, n + 1):
            if sqrt(num) % 1 == 0:
                dp[num] = 1
            else:
                index = 1
                while index**2 <= num:
                    dp[num] = min(dp[num], dp[index**2] + dp[num - index**2])
                    index += 1

        return dp[-1]
