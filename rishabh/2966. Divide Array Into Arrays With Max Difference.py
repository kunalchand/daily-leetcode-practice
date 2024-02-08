from typing import List
class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        
        # make sub arrays
        res = []
        i, l = 0, len(nums)

        while i < l:
            count = 0
            curr_window = []
            # make a window of 3
            while i < l and count < 3:
                curr_window.append(nums[i])
                i += 1
                count += 1
            
            if abs(curr_window[0] - curr_window[2]) > k: return []
            res.append(curr_window)
            # i += 1

        return res