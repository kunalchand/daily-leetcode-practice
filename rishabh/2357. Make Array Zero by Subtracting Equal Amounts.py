from typing import List
class Solution:

    '''
    Approach-2: Find non-zero unique elements
    Time: O(N)
    '''
    def minimumOperations(self, nums: List[int]) -> int:
        nums_set = set(nums)
        return len(nums_set) - 1 if 0 in nums_set else len(nums_set)


    '''
    Approach-1: Simulate the problem
    Time: O(N * K), K is the biggest value in nums
    '''
    def minimumOperations(self, nums: List[int]) -> int:
        operation_count = 0
        
        while sum(nums) > 0:
            min_val = float('inf')
            # find non-zero min value
            for n in nums:
                if n != 0:
                    min_val = min(min_val, n)

            # subtract this min_val from each n
            for idx, n in enumerate(nums):
                if n != 0:
                    nums[idx] = n - min_val
            
            operation_count += 1
        return operation_count
    

    

nums = [1,5,0,3,5]
print(Solution().minimumOperations(nums))