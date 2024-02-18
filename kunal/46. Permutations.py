from typing import List


class Solution:
    def generateNewAddon(self, index: int, addon: List[int]) -> List[int]:
        new_addon = addon[:]
        new_addon.pop(index)
        return new_addon

    def helper(self, ongoing: List[int], addon: List[int]) -> List[List[int]]:
        if len(addon) == 0:
            return [ongoing]
        else:
            ans = []
            for index, item in enumerate(addon):
                permutations = self.helper(ongoing, self.generateNewAddon(index, addon))
                for permutation in permutations:
                    ans.append(ongoing + [item] + permutation)

            return ans

    def permute(self, nums: List[int]) -> List[List[int]]:
        return self.helper([], nums)
