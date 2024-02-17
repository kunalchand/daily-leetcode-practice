from typing import List


class Solution:
    # Recursive Approach
    def __init__(self):
        self.ans = []

    def helper(self, base: List[int], addon: List[int]) -> None:
        for index, item in enumerate(addon):
            new_base = base[:] + [item]
            self.ans.append(new_base)
            self.helper(new_base, addon[index + 1 :])

    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Subset Size 0
        self.ans.append([])

        # Subset Size 1
        for num in nums:
            self.ans.append([num])

        # Subset Size 2 and more
        for index, num in enumerate(nums):
            self.helper([num], nums[index + 1 :])

        return self.ans
