class Solution:
    def findMax(self, arr, start, end) -> int:
        max_ = 0

        for i in range(start, end + 1):
            max_ = max(max_, arr[i])

        return max_

    def maxSumAfterPartitioning(self, arr: list[int], k: int) -> int:
        dp = []
        dp.append(0)
        # dp = [0 for i in range(len(arr) + 1)]

        for i in range(len(arr)):
            # exclude a[i] from the ongoing subarray
            exclude = arr[i] + dp[i]

            # include a[i] in the ongoing subarray
            start = i - k + 1 if i - k + 1 >= 0 else 0
            end = i

            include = 0
            while start <= end:
                include = max(
                    include,
                    dp[start] + ((end - start + 1) * self.findMax(arr, start, end)),
                )
                start += 1

            dp.append(max(exclude, include))
            # dp[i + 1] = max(exclude, include)

        return dp[-1]


print(Solution().maxSumAfterPartitioning([1, 15, 7, 9, 2, 5, 10], 3))
print(Solution().maxSumAfterPartitioning([1, 4, 1, 5, 7, 3, 6, 1, 9, 9, 3], 4))
print(Solution().maxSumAfterPartitioning([1], 1))
print(Solution().maxSumAfterPartitioning([6, 1, 9, 9, 3], 4))
