class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        subarray_count = len(nums) // 3
        ans = [[] for _ in range(subarray_count)]

        nums.sort()

        for i in range(0, len(nums), +3):
            if (nums[i + 2] - nums[i]) <= k:
                ans[i // 3].extend([nums[i], nums[i + 1], nums[i + 2]])
            else:
                return []

        return ans
