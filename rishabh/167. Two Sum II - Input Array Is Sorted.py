from typing import List
class Solution:
    '''
    we could've used 2 sum's solution, but we can't use extra space (hash-map)
    '''
    
    '''
    APPROACH - 1: Brute force with binary search
    traverse list, for a given number find its complement in the remaining list using binary search
    TIME: O(N * log N)
    SPACE: O(1)
    '''
    def twoSum_approach_1(self, numbers: List[int], target: int) -> List[int]:
        def binary_search(start_idx: int, complement: int) -> int:
            left, right = start_idx, len(numbers) - 1
            while (left <= right):
                mid = (left + right) // 2                            # int division
                if numbers[mid] == complement: return mid
                elif complement > numbers[mid]: left = mid + 1       # c lies in second half
                elif complement < numbers[mid]: right = mid - 1      # c lies in first half
            return - 1


        for idx, ele in enumerate(numbers):                       
            complement_idx = binary_search(idx+1, target-ele)
            if complement_idx != -1:
                return [idx + 1, complement_idx + 1]                # add 1 to answer

    '''
    APPROACH - 2: 2 pointers, start and end
    curr_sum = n[start] + n[end]
    move end towards left if target < curr_sum, it means curr_sum is too large, we need smaller values
    move start towards right if target > curr_sum, it means curr_sum is too small, we need greater values for curr_sum to go big
    TIME: O(N * log N)
    SPACE: O(1)
    '''
    '''
    :param numbers: A sorted list of integers.
    :param target: The target integer that the sum of the two numbers should equal to.
    :return: A list containing the indices (1-indexed) of the two numbers that add up to the target.
                If no such pair is found, returns [None, None].
    '''
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start, end = 0, len(numbers) - 1
        while start < end:
            curr_sum = numbers[start] + numbers[end]
            if curr_sum == target:
                return [start + 1, end + 1]             # Return the indices of the two numbers
            elif curr_sum > target:
                end -= 1                                # Decrement end pointer if the sum is greater than the target
            elif curr_sum < target:
                start += 1                              # Increment start pointer if the sum is less than the target
        return [None, None]                             # If no such pair is found, return [None, None]


    def test_twoSum(self):
        solution = Solution()

        # Test case where the target is present in the list
        assert solution.twoSum([2, 7, 11, 15], 9) == [1, 2]

        # Test case where the target is not present in the list
        assert solution.twoSum([2, 7, 11, 15], 10) == [None, None]

        # Test case where the target is achieved by the first and last elements
        assert solution.twoSum([2, 7, 11, 15], 17) == [1, 4]

        # Test case where the list contains negative numbers
        assert solution.twoSum([-3, -2, -1, 0, 4, 7], -5) == [1, 2]

        # Test case where the list contains duplicate numbers
        assert solution.twoSum([1, 2, 2, 3, 4, 5], 4) == [2, 3] or [1,3]

        # Test case where the list contains only two elements and they add up to the target
        assert solution.twoSum([1, 2], 3) == [1, 2]

        # Test case where the list contains only two elements but they don't add up to the target
        assert solution.twoSum([1, 2], 5) == [None, None]

        print("All test cases passed successfully!")


# Run the test cases
Solution().test_twoSum()
