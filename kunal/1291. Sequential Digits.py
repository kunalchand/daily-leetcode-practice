class Solution:
    def sequentialDigits(self, low: int, high: int) -> list[int]:
        fixed = "123456789"

        ans = []

        for i in range(len(str(low)), len(str(high)) + 1):
            left = 0
            right = left + i

            while right <= len(fixed):
                new_int = int(fixed[left:right])
                ans.append(new_int) if new_int >= low and new_int <= high else None
                left += 1
                right += 1

        return ans


print(Solution().sequentialDigits(100, 300))
print(Solution().sequentialDigits(1000, 13000))
