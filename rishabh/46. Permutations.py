from typing import List
class Solution:
    '''
    I/P - List[int]
        - unique
        - sorted/unsorted
        - minlen = 1
        - [a] [[a]]
        - +ve, -ve can be any

    O/P - List[List[int]]
        - all possible, in any order

    Approach:
        - brute-force => backtrack
        - build the whole path
        - swap
     
    TIME: O(N * N!)

    in approach 2 (build the whole path):
    Notice how len(curr) == len(nums) is a terminating condition 
    bcz each ans is same length as input

        eg: [1,2,3]
                               []
                  /             |            \
             [1]               [2]               [3]
            /   \            /     \            /   \
        [1,2]   [1,3]     [2,1]   [2,3]     [3,1]   [3,2]
         |        |         |        |        |        |
      [1,2,3]   [1,3,2]   [2,1,3]  [2,3,1]  [3,1,2]  [3,2,1]


    '''

    '''
    APPROACH-1: SWAP
    '''
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def backtrack(start, curr_lst):
            # base case
            if start == len(nums) - 1:
                ans.append(curr_lst.copy())
                return
            
            for i in range(start, len(nums)):
                curr_lst[start], curr_lst[i] = curr_lst[i], curr_lst[start]     # swap
                backtrack(start + 1, curr_lst)
                curr_lst[start], curr_lst[i] = curr_lst[i], curr_lst[start]     # swap back (backtrack)

        backtrack(0, nums)
        return ans


    '''
    APPROACH-2: build from empty path and add that whole path to res
    '''
    def permute2(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(curr_path):
            if len(curr_path) == len(nums):
                res.append(curr_path.copy())
                return 
            
            for n in nums:
                # skip elements that are already present in curr_path
                if n not in curr_path:
                    curr_path.append(n)
                    backtrack(curr_path)
                    curr_path.pop()

        backtrack([])
        return res
    
    '''
    APPROACH-3: same as above but a little different in the sense that here we are explicitly taking the ele out which we don't want in current iteration
    whereas in above method we are checking everything and calling the func for only those eles that are not present in the curr_path
    build from empty path and add that whole path to res
    '''
    def permute3(self, nums: List[int]) -> List[List[int]]:
        l = len(nums)
        output = []
        res_path = []

        def dfs(curr_list):
            if len(res_path) == l:
                output.append(res_path[:])
                return
                                                            
            for idx, ele in enumerate(curr_list):
                res_path.append(ele)
                temp = curr_list.pop(idx)                   
                
                dfs(curr_list[:])
                
                curr_list.insert(idx, temp)
                res_path.pop()
            
        dfs(nums[:])
        return output


nums = [1,2,3]              # [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# nums = [1]                  # [[1]]
# nums = [0,1]                # [[0,1],[1,0]]
print(Solution().permute2(nums))