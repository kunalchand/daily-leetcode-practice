from typing import List

class Solution:
    '''
    APPROACH-1: FLOYD'S FAST & SLOW to find the cycle AND
    FIND START OF CYCLE USING 'start' and 'slow' pointers
    start of a cycle is a node where multiple nodes point to it
    TIME: O(N)
    SPACE: O(1)
    '''
    def findDuplicate(self, nums: List[int]) -> int:
        # find the cycle using floyd's fast and slow pointers
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast: break          # break out of the cycle as soon as you find a cycle
        
        # if you start a pointer from start of the list
        # and keep moving the slow pointer
        # eventually, both pointers will point to duplicate elements
        # why? it's a given algorithm like, floyd's fast and slow pointers
        # intuition: slow will keep on moving in cycle and start will travel towards this cycle
        # there'll be a time when both start and slow will point to a duplicate number
        start = 0
        while True:
            slow = nums[slow]
            start = nums[start]
            if slow == start: return slow # or return start
    
    '''
    APPROACH-2: Brute Force
    TIME: O(N)
    SPACE: O(1)
    '''
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]: return nums[i]

    '''
    Other Approach: changing the list is not allowed but just an idea
    use binary search to find the duplicate element instead of linear search 
    TIME: O(N * log N)
    SPACE: O(1)
    '''
    def findDuplicate(self, nums: List[int]) -> int:
        
        def binary_search(target, start):
            l, r = start, len(nums) - 1
            while l <= r:
                mid = (l+r)//2
                if nums[mid] == target: return True
                elif nums[mid] > target: r = mid - 1
                elif nums[mid] < target: l = mid + 1

        nums.sort()
        for i in range(len(nums)):
            if binary_search(nums[i],i+1):
                return nums[i]
        return -1


nums = [1,3,4,2,2]
print(Solution().findDuplicate(nums))