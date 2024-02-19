from typing import List


class Solution:
    def __init__(self):
        self.hashset = set()

    def helper(self, ongoing: List[int], addon: List[int]) -> None:
        self.hashset.add(tuple(ongoing))

        if len(addon) == 0:
            return
        else:
            for index, item in enumerate(addon):
                self.helper(ongoing + [item], addon[index + 1 :])

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # Tuple Order in set matter. (1,4) and (4,1) have different hash
        nums.sort()

        # Subset Size 0
        self.hashset.add(())

        # Subset Size 1 and more
        for index, item in enumerate(nums):
            self.helper([item], nums[index + 1 :])

        ans = []

        for element in self.hashset:
            ans.append(list(element))

        return ans


print(Solution().subsetsWithDup([1, 2, 2]))
print(Solution().subsetsWithDup([0]))
