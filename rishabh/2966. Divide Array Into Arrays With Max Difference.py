from typing import List
class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        
        # Approach: sort
        # make sub arrays of size 3 and append to res
        # if it's an invalid subarray (diff > k), then return []
        # TIME: O(n * log n)
        '''
        nums.sort()
        res = []
        i, l = 0, len(nums)

        while i < l:
            count = 0
            curr_window = []                    # sub array
            
            while i < l and count < 3:          # make a window of size 3
                curr_window.append(nums[i])
                i += 1
                count += 1
            
            if abs(curr_window[0] - curr_window[2]) > k: return []
            res.append(curr_window)
            
        return res
        '''
        # same code as above but cleaner
        nums.sort()
        res = []

        for i in range(0, len(nums), 3):
            if nums[i + 2] - nums[i] > k: return []                 # return if sub array is invalid
            res.append([nums[i], nums[i + 1], nums[i + 2]])
        
        return res
    


obj = Solution()
nums = [1,3,4,8,7,9,3,5,1]
k = 2
print(obj.divideArray())