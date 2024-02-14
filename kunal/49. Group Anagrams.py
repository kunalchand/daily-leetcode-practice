from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_ = defaultdict(list)

        for string in strs:
            sorted_string = "".join(sorted(string))
            dict_[sorted_string].append(string)

        ans = []

        for value_list in dict_.values():
            ans.append(value_list)

        return ans


print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
