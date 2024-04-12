'''
Given an integer array nums, return the number of non-empty subarrays with the leftmost element of the subarray not larger than other elements in the subarray.

A subarray is a contiguous part of an array.

 

Example 1:

Input: nums = [1,4,2,5,3]
Output: 11
Explanation: There are 11 valid subarrays: [1],[4],[2],[5],[3],[1,4],[2,5],[1,4,2],[2,5,3],[1,4,2,5],[1,4,2,5,3].
Example 2:

Input: nums = [3,2,1]
Output: 3
Explanation: The 3 valid subarrays are: [3],[2],[1].
Example 3:

Input: nums = [2,2,2]
Output: 6
Explanation: There are 6 valid subarrays: [2],[2],[2],[2,2],[2,2],[2,2,2].
 

Constraints:

1 <= nums.length <= 5 * 104
0 <= nums[i] <= 105

'''
from typing import List
class Solution:
    '''
    [3,2,1]
    [3,2]
    [2,1]

    [       a    c d   b     ]    

    [2,4,1,5,3] -inf
    [24] [15] [153]
    

    [1 1 4 3 4] 
    1 - 0 + 1 = 2 => [2] [2,4]
    1 - 1 + 1 = 1 => [4]
    4 - 2 + 1 = 3 => [1] [15] [153]
    5 - 


    [4,5,6,3,2]
    [    3 2 2]

    T[2 3]B

    min = 1
    min_idx = 2

    [1,2,3,4]
    [3 3 3 3]
    3 - 0 + 1 => 4

    '''
    def validSubarrays(self, nums: List[int]) -> int:

        # traverse from Right to Left
        # on the way push/pop on stack and calculate answer

        mono_incr_stack = [[float('-inf'), len(nums)]]
        count = 0
        val, index = 0, 1
        
        # keep popping until curr_ele <= top, calculate distance, push onto stack
        for idx in range(len(nums) - 1, -1, -1):
            curr_val = nums[idx]
            while curr_val <= mono_incr_stack[-1][val]:
                mono_incr_stack.pop()
                
            count += mono_incr_stack[-1][index] - idx
            mono_incr_stack.append([curr_val, idx])

        return count
    
    
nums = [2,4,1,5,3]      # 8
nums = [1,4,2,5,3]      # 11
# nums = [3,2,1]          # 3
# nums = [2,2,2]          # 6
print(Solution().validSubarrays(nums))