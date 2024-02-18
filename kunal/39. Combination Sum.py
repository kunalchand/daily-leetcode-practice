from typing import List


class Solution:
    def __init__(self):
        self.ans = []

    def helper(self, ongoing: List[int], addon: List[int], target: int) -> None:
        if sum(ongoing) > target:
            return
        elif sum(ongoing) == target:
            self.ans.append(ongoing)
        else:
            for index, item in enumerate(addon):
                self.helper(ongoing + [item], addon[index:], target)

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        for index, item in enumerate(candidates):
            self.helper([item], candidates[index:], target)

        return self.ans
