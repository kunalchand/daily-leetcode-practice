class Solution:
    def divideArray(self, nums: list[int], k: int) -> list[list[int]]:
        subarray_count = len(nums) // 3
        ans = [[] for _ in range(subarray_count)]

        nums.sort()

        for i in range(0, len(nums), +3):
            if (nums[i + 2] - nums[i]) <= k:
                ans[i // 3].extend([nums[i], nums[i + 1], nums[i + 2]])
            else:
                return []

        return ans


print(Solution().divideArray([1, 3, 4, 8, 7, 9, 3, 5, 1], 2))
print(Solution().divideArray([1, 3, 3, 2, 7, 3], 3))
