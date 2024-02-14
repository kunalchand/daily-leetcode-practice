class Solution:
    def returnSmallest(self, s1, s2) -> str:
        if s1 == "":
            return s2
        elif len(s1) > len(s2):
            return s2
        else:
            return s1

    def minWindow(self, s: str, t: str) -> str:
        t_dict = {}

        for t_char in t:
            t_dict[t_char] = t_dict.get(t_char, 0) + 1

        t_count = len(t_dict)

        left = 0
        right = 0

        min_string = ""

        while right < len(s):
            while right < len(s) and t_count != 0:
                s_char = s[right]
                if s_char in t_dict:
                    t_dict[s_char] -= 1
                    if t_dict[s_char] == 0:
                        t_count -= 1
                right += 1

            if t_count == 0:
                min_string = self.returnSmallest(min_string, s[left:right])

            while left < right and t_count == 0:
                s_char = s[left]
                if s_char in t_dict:
                    t_dict[s_char] += 1
                    if t_dict[s_char] == 1:
                        t_count += 1
                    else:
                        min_string = self.returnSmallest(
                            min_string, s[left + 1 : right]
                        )
                else:
                    min_string = self.returnSmallest(min_string, s[left + 1 : right])
                left += 1

        return min_string


print(Solution().minWindow("ADOBECODEBANC", "ABC"))
print(Solution().minWindow("a", "a"))
print(Solution().minWindow("a", "aa"))
print(Solution().minWindow("ADOBECODEBANC", "AABC"))
