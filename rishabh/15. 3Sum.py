from typing import List

# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
# https://leetcode.com/problems/3sum/description/

class Solution:
    '''
    APPROACH: 2 Pointers, use concept of 2-SUM-II (start and end pointer, move according to sum and target)
    TIME: O(N * log N)
    SPACE: O(N), python takes extra space for sorting (temporarily though)
    '''
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Finds all unique triplets in the array that sum up to zero.

        :param nums: A list of integers representing the input array.
        :rtype: List[List[int]]
        :return: A list of lists containing unique triplets that sum up to zero.
        """
        n, target = len(nums) - 1, 0
        res = []
        
        nums.sort()                                                                     # sort to use 2 sum - II concepts of 2 pointers
        for idx in range(n-1):                                                          # traversing till last 3rd value, loop will run till (n-2). 1,2,3, ... , n-3, n-2, n-1, n
            if nums[idx] > 0:                                                           # skip if curr value is +ve, sum can't be 0 then
                continue
            if idx > 0 and nums[idx - 1] == nums[idx]:                                  # skip duplicates, make sure to skip the second duplicate not the first
                continue
            
            l, r = idx + 1, n
            while l < r:
                three_sum = nums[idx] + nums[l] + nums[r]
                if three_sum < target:
                    l += 1
                elif target < three_sum:
                    r -= 1
                elif target == three_sum:
                    res.append([nums[idx], nums[l], nums[r]])
                    l, r = l + 1, r - 1

                    while l < r and nums[l-1] == nums[l]:
                        l += 1
                    while l < r and nums[r + 1] == nums[r]:
                        r -= 1
        return res

    def test_threeSum(self):
        sol = Solution()

        # Test case 1: Regular case with multiple solutions
        nums1 = [-1, 0, 1, 2, -1, -4]
        assert sol.threeSum(nums1) == [[-1, -1, 2], [-1, 0, 1]], "Test case 1 failed"

        # Test case 2: No solution
        nums2 = [1, 2, 3, 4]
        assert sol.threeSum(nums2) == [], "Test case 2 failed"

        # Test case 3: All zeros
        nums3 = [0, 0, 0]
        assert sol.threeSum(nums3) == [[0, 0, 0]], "Test case 3 failed"

        # Test case 4: All positive numbers
        nums4 = [1, 2, 3, 4, 5]
        assert sol.threeSum(nums4) == [], "Test case 4 failed"

        # Test case 5: All negative numbers
        nums5 = [-5, -4, -3, -2, -1]
        assert sol.threeSum(nums5) == [], "Test case 5 failed"

        print("All test cases passed successfully!")

# Run the test cases
Solution().test_threeSum()