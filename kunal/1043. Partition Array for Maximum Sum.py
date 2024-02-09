class Solution:
    def maxSum(self, dp, arr, start, end, k) -> int:
        maxValue = float("-inf")
        maximumSum = float("-inf")

        while start >= 0 and (end - start + 1) <= k:
            maxValue = max(maxValue, arr[start])
            maximumSum = max(maximumSum, dp[start] + ((end - start + 1) * maxValue))
            start -= 1

        return maximumSum

    def maxSumAfterPartitioning(self, arr: list[int], k: int) -> int:
        dp = []
        dp.append(0)

        for i in range(len(arr)):
            # exclude arr[i] from the ongoing subarray
            exclude = dp[i] + arr[i]

            # include arr[i] in the ongoing subarray
            include = self.maxSum(dp, arr, i, i, k)

            dp.append(max(exclude, include))

        return dp[-1]


print(Solution().maxSumAfterPartitioning([1, 15, 7, 9, 2, 5, 10], 3))
print(Solution().maxSumAfterPartitioning([1, 4, 1, 5, 7, 3, 6, 1, 9, 9, 3], 4))
print(Solution().maxSumAfterPartitioning([1], 1))
print(Solution().maxSumAfterPartitioning([6, 1, 9, 9, 3], 4))
