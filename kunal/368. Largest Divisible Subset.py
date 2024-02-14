from typing import List


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()

        dp = [[nums[i]] for i in range(len(nums))]

        for i in range(1, len(nums)):
            max_length = float("-inf")
            for j in range(i, 0, -1):
                dp_list = dp[j - 1]
                if nums[i] % dp_list[-1] == 0:
                    if len(dp_list) + 1 > max_length:
                        dp[i] = dp_list + [dp[i][-1]]
                        max_length = len(dp[i])

        return max(dp, key=len, default=[])

        """
        max_length = float('-inf')
        max_list = []
        for dp_list in dp:
            if max_length < len(dp_list):
                max_length = len(dp_list)
                max_list = dp_list
        
        return max_list
        """


print(Solution().largestDivisibleSubset([1, 2, 3]))
print(Solution().largestDivisibleSubset([1, 2, 4, 8]))
print(Solution().largestDivisibleSubset([4, 8, 10, 240]))
