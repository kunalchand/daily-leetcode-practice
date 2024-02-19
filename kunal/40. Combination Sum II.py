from typing import List


class Solution:
    def __init__(self):
        self.ans = []

    def helper(
        self, ongoing: List[int], addon: List[int], freq: List[int], target: int
    ) -> None:
        if sum(ongoing) == target:
            self.ans.append(ongoing)
            return
        elif sum(ongoing) > target:
            return
        else:
            for index, item in enumerate(addon):
                new_freq = freq[index:]
                new_freq[0] -= 1
                if new_freq[0] > 0:
                    self.helper(ongoing + [item], addon[index:], new_freq, target)
                elif new_freq[0] == 0:
                    self.helper(
                        ongoing + [item], addon[index + 1 :], freq[index + 1 :], target
                    )

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        dict_ = {}

        for candidate in candidates:
            dict_[candidate] = dict_.get(candidate, 0) + 1

        addon = []
        freq = []
        for key, value in dict_.items():
            addon.append(key)
            freq.append(value)

        self.helper([], addon, freq, target)

        return self.ans


print(Solution().combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
print(Solution().combinationSum2([2, 5, 2, 1, 2], 5))
