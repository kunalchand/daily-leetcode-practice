from typing import List
# https://leetcode.com/problems/longest-consecutive-sequence/

class Solution:
    '''
    I/O:
        int array, unsorted, -ve, 0, +ve, repeatition allowed
    Clarifying Questions:
        What do you mean by Consecutive?
        Ans => n, n+1, n+2, ...
    Constraints:
        solve in O(n) 
    Edge Cases:
        repeat, empty input
    Approach:
        A) Brute Force:                             Time Complexity: O(n log n) + O(n)
        - first sort                                O(n log n) 
        - and then check consecutive elements       O(n)
        I/P = [10, 11, 12, 13, 4, 20, 1, 3]
        sorted_ip = [1,3,4,10,11,12,13,20]
        [3,4] [10,11,12,13] [11,12,13] [12,13]

        Optimized:
            hash table, set, check existance of next element, multiple passes
            at each element check if it's a start of the sequence or not
            by checking if n-1 exists in the array.
            If n-1 exists in array, n can't be start of a seq, therefore, skip it 
            else consider it a start of the sequence and start a streak

    Test Cases Dry Run:
        T1: [4,8,7,3,1,2,-1,6,0]
        
        [-1,0,1,2,3,4] [6,7,8]
        curr_ele = 8
        curr_len = 3
        max_len = 6

        T2: [15,3,4,10,2,11,12,13,1,14]

        [3,4] [10,11,12,13,14,15] [2,3,4]
        curr_ele = 4
        curr_len = 3
        max_len = 5
    '''

    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        curr_len, max_len = 0,0

        for n in nums:
            if n-1 not in num_set:
                # n can be a start of seq
                curr_ele = n
                curr_len = 1

                # find the whole seq
                curr_seq = []                   # not necessary
                curr_seq.append(curr_ele)       # not necessary
                while curr_ele+1 in num_set:
                    curr_ele += 1
                    curr_len += 1
                    curr_seq.append(curr_ele)   # not necessary
                
                print(curr_seq)                 # not necessary
                max_len = max(max_len, curr_len)

        return max_len


    '''
    APPROACH - 2: brute force
    sort 
    traverse array
    and keep checking next element until end
    TIME: O(N ^ 2), traverse array
    SPACE: O(1)
    ONLY WORKS FOR NON-REPEATING INPUT
    '''
    def longestConsecutive_brute_force(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        nums.sort()
        max_len = 1

        for i in range(len(nums)):
            curr_seq = [nums[i]]
            curr_len = 1

            for j in range(i, len(nums) - 1):
                curr_ele, next_ele = nums[j], nums[j + 1]

                if next_ele != curr_ele + 1:
                    break
                else:
                    curr_len += 1
                    curr_seq.append(next_ele)

                max_len = max(max_len, curr_len)
            print(curr_seq)
        return max_len



print(Solution().longestConsecutive([0,3,7,2,5,8,4,6,0,1]))