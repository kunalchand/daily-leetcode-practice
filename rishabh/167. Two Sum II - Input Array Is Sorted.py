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
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
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
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start, end = 0, len(numbers) - 1
        while start < end:
            curr_sum = numbers[start] + numbers[end]
            if curr_sum == target: return [start + 1, end + 1]
            elif curr_sum > target: end -= 1
            elif curr_sum < target: start += 1
        return [None, None]